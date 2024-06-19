#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:59:36 2018

@author: Fraser M Callaghan

Classes for building standardised imaging projects. 
Adapted for general use from KMR project. 


"""


import os
import re
from zipfile import ZipFile
import numpy as np
import datetime
import pandas as pd
import shutil
import logging
##
from spydcmtk import spydcm
from miresearch import mi_utils

# ====================================================================================================
# ====================================================================================================

# ====================================================================================================
#       ABSTRACT SUBJECT CLASS
# ====================================================================================================
class AbstractSubject(object):
    """
    An abstract subject controlling most basic structure
    """
    def __init__(self, subjectNumber, 
                        dataRoot, 
                        subjectPrefix=None,
                        DIRECTORY_STRUCTURE_TREE=mi_utils.buildDirectoryStructureTree(),
                        padZeros=mi_utils.MIResearch_config.default_pad_zeros,
                        suffix="") -> None:
        # -- CHECK REQUIRED INPUT --
        if subjectNumber is None:
            raise ValueError(f"Give subjectNumber (as int) or as subjID")
        self.dataRoot = dataRoot
        self._subjID = None
        if not os.path.isdir(self.dataRoot):
            raise ValueError(f"'dataRoot' must be a directory and must exist: Not found: {self.dataRoot}")
        # -- PROCESS INPUT ##
        # A) subjectNumber is an int
        try:
            self._subjN = int(subjectNumber)
            if subjectPrefix is None:
                # not given - guess from others in dataRoot
                subjectPrefix = guessSubjectPrefix(self.dataRoot, QUIET=True) # will raise mi_utils.SubjPrefixError if not obvious
            self.subjectPrefix = subjectPrefix
        except ValueError: # fail on int 
            # B) subjectNumber not an int - then treat as subjectID
            #       first check if can split to prefix, N, suffix
            try:
                prefix_N_suffix = splitSubjID(subjectNumber)
                self.subjectPrefix = prefix_N_suffix[0]
                self._subjN = prefix_N_suffix[1]
                if len(prefix_N_suffix) == 3:
                    suffix = prefix_N_suffix[2]
                padZeros = findZeroPadding(subjectNumber)
            except IndexError: 
                self._subjID = subjectNumber

        self.suffix = suffix
        self.padZeros = padZeros
        self.DIRECTORY_STRUCTURE_TREE = DIRECTORY_STRUCTURE_TREE
        self.BUILD_DIR_IF_NEED = True
        self.dicomMetaTagList = mi_utils.DEFAULT_DICOM_META_TAG_LIST
        self.QUIET = False
        #
        self._logger = None
        self._loggerFH = None


    ### ----------------------------------------------------------------------------------------------------------------
    ### Class Methods
    ### ----------------------------------------------------------------------------------------------------------------

    ### ----------------------------------------------------------------------------------------------------------------
    ### Overriding methods
    ### ----------------------------------------------------------------------------------------------------------------
    def __hash__(self):
        return hash((self.subjID, self.dataRoot))

    def __eq__(self, other):
        try:
            return (self.subjID == other.subjID) & \
                   (self.dataRoot == other.dataRoot)
        except AttributeError:
            return False

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.getPrefix_Number()[1] < other.getPrefix_Number()[1]

    def __str__(self):
        return f"{self.subjID} at {self.dataRoot}"

    ### ----------------------------------------------------------------------------------------------------------------
    ### Properties
    ### ----------------------------------------------------------------------------------------------------------------
    @property
    def subjID(self):
        if self._subjID is not None:
            return self._subjID
        return buildSubjectID(self._subjN, self.subjectPrefix, padZeros=self.padZeros, suffix=self.suffix)

    @property
    def subjN(self):
        return splitSubjID(self.subjID)[1]
    ### ----------------------------------------------------------------------------------------------------------------
    ### Logging
    ### ----------------------------------------------------------------------------------------------------------------
    @property
    def logger(self):
        if self._logger is None:
            rr = os.path.split(self.dataRoot)[1]
            self._logger = logging.getLogger(f"{rr}/{self.subjID}")
            self._logger.setLevel(logging.INFO)
            self._loggerFH = logging.FileHandler(self.logfileName)
            self._loggerFH.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-7s | %(name)s | %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
            self._logger.addHandler(self._loggerFH)
            if not self.QUIET:
                self._logger.addHandler(logging.StreamHandler())
        return self._logger

    @property
    def logfileName(self):
        return os.path.join(self.getMetaDir(), f'{self.subjID}.log')

    def _renameLogger(self):
        """Rename the logger - is run from method renameSubjID
        """
        self._loggerFH.close()
        self.logger.removeHandler(self._loggerFH)
        self._loggerFH = None
        self._loggerFH = logging.FileHandler(self.logfileName, mode='a')
        self._loggerFH.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-7s | %(name)s | %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
        self._logger.addHandler(self._loggerFH)

    ### ----------------------------------------------------------------------------------------------------------------
    ### Methods
    ### ----------------------------------------------------------------------------------------------------------------
    def initDirectoryStructure(self):
        if os.path.isdir(self.getTopDir()):
            self.logger.info(f"Study participant {self.subjID} exists at {self.getTopDir()}. Updating directory structure")
        os.makedirs(self.getTopDir(), exist_ok=True)
        for i in self.DIRECTORY_STRUCTURE_TREE:
            os.makedirs(os.path.join(self.getTopDir(), i.name), exist_ok=True)
            for j in i.childrenList:
                os.makedirs(os.path.join(self.getTopDir(), i.name, j), exist_ok=True)
        self.logger.info(f"Directory structure correct for {self.subjID} at {self.getTopDir()}.")

    def getPrefix_Number(self):
        return splitSubjID(self.subjID)

    ### LOADING -------------------------------------------------------------------------------------------------------
    def loadDicomsToSubject(self, dicomFolderToLoad, anonName=None, HIDE_PROGRESSBAR=False):
        self.initDirectoryStructure()
        self.logger.info(f"LoadDicoms to {self.getDicomsDir()}") # Don't log source here as could be identifying
        self.logger.debug(f"LoadDicoms ({dicomFolderToLoad} ==> {self.getDicomsDir()}) & anon={anonName}") 
        d0, dI = self.countNumberOfDicoms(), mi_utils.countFilesInDir(dicomFolderToLoad)
        study = spydcm.dcmTK.DicomStudy.setFromDirectory(dicomFolderToLoad, HIDE_PROGRESSBAR=HIDE_PROGRESSBAR)
        res = study.writeToOrganisedFileStructure(self.getDicomsDir())
        self._finalLoadSteps(d0, dI, anonName)

    def loadSpydcmStudyToSubject(self, spydcmData, anonName=None):
        self.initDirectoryStructure()
        self.logger.info(f"LoadDicoms (spydcmtk data ==> {self.getDicomsDir()})")
        d0, dI = self.countNumberOfDicoms(), spydcmData.getNumberOfDicoms()
        spydcmData.writeToOrganisedFileStructure(self.getDicomsDir())
        self._finalLoadSteps(d0, dI, anonName=anonName)
    
    def _finalLoadSteps(self, initNumDicoms, numDicomsToLoad, anonName=None):
        self.buildDicomMeta()
        if anonName is not None:
            self.anonymise(anonName=anonName)
        finalNumDicoms = self.countNumberOfDicoms()
        self.logger.info(f"Initial number of dicoms: {initNumDicoms}, number to load: {numDicomsToLoad}, final number dicoms: {finalNumDicoms}")
        self.buildDicomMeta()
        self.buildSeriesDataMetaCSV(FORCE=True)
        self.runPostLoadPipeLine()

    def runPostLoadPipeLine(self, *args, **kwargs):
        # this is an abstract method for implementation by subclasses
        pass

    ### FOLDERS / FILES ------------------------------------------------------------------------------------------------
    def exists(self):
        return os.path.isdir(self.getTopDir())

    def getTopDir(self):
        return os.path.join(self.dataRoot, self.subjID)

    def _getDir(self, listOfDirsBeyondStudyDir, BUILD_IF_NEED=True):
        if type(listOfDirsBeyondStudyDir) != list:
            raise ValueError(f"_getDir takes a list as first argument")
        dd = os.path.join(self.getTopDir(), *listOfDirsBeyondStudyDir)
        if not os.path.isdir(dd):
            if BUILD_IF_NEED & self.BUILD_DIR_IF_NEED:
                if not os.path.isdir(self.getTopDir()):
                    raise IOError(f"{self.getTopDir()} does not exist")
                os.makedirs(dd, exist_ok=True)
        return dd

    def getMetaDir(self):
        return self._getDir([mi_utils.META])

    def getRawDir(self):
        return self._getDir([mi_utils.RAW])
    
    def getDicomsDir(self):
        dirName = self._getDir([mi_utils.RAW, mi_utils.DICOM])
        return dirName
    
    def renameSubjID(self, newSubjID):
        oldID = self.subjID
        if newSubjID == oldID:
            self.logger.error(f"Can not rename from {oldID} to {newSubjID}")
            return
        self.logger.warning(f"Changing subjID from {oldID} to {newSubjID}")
        self.logger.warning(" *** THIS WILL LIKELY HAVE BREAKING CONSEQUENCES ***")
        newName = os.path.join(self.dataRoot, newSubjID)
        if os.path.isdir(newName):
            shutil.rmtree(newName)
        os.rename(self.getTopDir(), newName)
        self.subjectPrefix = newSubjID
        self._subjN = None
        self._renameLogger()
        self.logger.warning(f"New logger after subjID changed from {oldID} to {self.subjID}")
        self.logger.warning(" *** THIS WILL LIKELY HAVE BREAKING CONSEQUENCES ***")        
        self.buildDicomMeta()
        self.buildSeriesDataMetaCSV(FORCE=True)

    ### META STUFF -----------------------------------------------------------------------------------------------------
    def getSeriesMetaCSV(self):
        return os.path.join(self.getMetaDir(), 'ScanSeriesInfo.csv')

    def getSeriesMetaAsDataFrame(self):
        return pd.read_csv(self.getSeriesMetaCSV(),  encoding="ISO-8859-1")

    def buildSeriesDataMetaCSV(self, FORCE=False):
        if os.path.isfile(self.getSeriesMetaCSV()) and (not FORCE):
            return 
        seInfoList = []
        dcmStudies = spydcm.dcmTK.ListOfDicomStudies.setFromDirectory(self.getDicomsDir(), HIDE_PROGRESSBAR=True)
        for dcmStudy in dcmStudies:
            for dcmSE in dcmStudy:
                iSerDict = dcmSE.getSeriesInfoDict(["SeriesNumber", 
                                                            "SeriesDescription", 
                                                            "StudyDate", 
                                                            "AcquisitionTime",
                                                            "InPlanePhaseEncodingDirection", 
                                                            "PixelBandwidth",
                                                            ])
                seInfoList.append(iSerDict)
        df = pd.DataFrame(data=seInfoList)
        df.to_csv(self.getSeriesMetaCSV())
        self.logger.info('buildSeriesDataMetaCSV')

    def info(self):
        # Print info for this subject
        return f"{self.subjID}: {self.getName()} scanned on {self.getStudyDate()}"

    def printDicomsInfo(self):
        dicomFolderList = self.getDicomFoldersListStr(False)
        print(str(self))
        ss = ["    " + i for i in dicomFolderList]
        print("\n".join(ss))
        print("")

    def askUserForDicomSeriesNumber(self):
        self.printDicomsInfo()
        seNum = input("Enter the dicom series number: ")
        return int(seNum)

    def findDicomSeries(self, descriptionStr, excludeStr=None):
        return self.getSeriesNumbersMatchingDescriptionStr(descriptionStr, excludeStr=excludeStr)

    def getStartTime_EndTimeOfExam(self):
        NN = self.getListOfSeNums()
        Ns = min(NN)
        Ne = max([i for i in NN if i < 99])
        df = self.getSeriesMetaAsDataFrame()
        t2 = self.getStartTimeForSeriesN_HHMMSS(Ne, df=df)
        t2 = mi_utils.timeToDatetime(str(t2))
        endT = t2 + datetime.timedelta(0, self.getTimeTakenForSeriesN_s(Ne, df=df))
        endT_HHMMSS = datetime.datetime.strftime(endT, '%H%M%S')
        return self.getStartTimeForSeriesN_HHMMSS(Ns), endT_HHMMSS

    def getTimeTakenForSeriesN_s(self, N, df=None):
        if df is None:
            df = self.getSeriesMetaAsDataFrame()
        return list(df.loc[df['SeriesNumber']==N,'ScanDuration'])[0]

    def getHRForSeriesN(self, N, df=None):
        if df is None:
            df = self.getSeriesMetaAsDataFrame()
        return list(df.loc[df['SeriesNumber']==N,'HeartRate'])[0]

    def getStartTimeForSeriesN_HHMMSS(self, N, df=None):
        if df is None:
            df = self.getSeriesMetaAsDataFrame()
        return list(df.loc[df['SeriesNumber']==N,'AcquisitionTime'])[0]

    def getDifferenceBetweenStartTimesOfTwoScans_s(self, seN1, seN2):
        df = self.getSeriesMetaAsDataFrame()
        t1 = self.getStartTimeForSeriesN_HHMMSS(seN1, df)
        t2 = self.getStartTimeForSeriesN_HHMMSS(seN2, df)
        t1 = mi_utils.timeToDatetime(str(t1))
        t2 = mi_utils.timeToDatetime(str(t2))
        return (t2-t1).seconds

    def getTotalScanTime_s(self):
        se = self.getListOfSeNums()
        se = [i for i in se if i < 1000]
        s1 = self.getDifferenceBetweenStartTimesOfTwoScans_s(min(se), max(se))
        s2 = self.getTimeTakenForSeriesN_s(max(se))
        return s1 + s2

    def findDicomSeries(self, descriptionStr):
        return self.getSeriesNumbersMatchingDescriptionStr(descriptionStr)

    def getSeriesNumbersMatchingDescriptionStr(self, descriptionStr): # FIXME what if mult studies
        dcmStudy = spydcm.dcmTK.DicomStudy.setFromDirectory(self.getDicomsDir(), HIDE_PROGRESSBAR=True, ONE_FILE_PER_DIR=True)
        dOut = {}
        for iSeries in dcmStudy:
            if descriptionStr.lower() in iSeries.getTag('SeriesDescription').lower():
                dOut[iSeries.getTag('SeriesNumber', ifNotFound='#')] = iSeries.getSeriesOutDirName()
        return dOut

    def getSeriesMetaValue(self, seNum, varName):
        """Get meta value for given series naumber

        Args:
            seNum (int): series number
            varName (str): tag name, from: EchoTime FlipAngle HeartRate
                InPlanePhaseEncodingDirection InternalPulseSequenceName PulseSequenceName
                RepetitionTime ScanDuration SeriesDescription
                SeriesNumber SpacingBetweenSlices StartTime
                dCol dRow dSlice dTime
                nCols nRow nSlice nTime

        Returns:
            ANY: tag value
        """
        df = self.getSeriesMetaAsDataFrame()
        return list(df.loc[df['SeriesNumber'] == seNum, varName])[0]

    def getDicomSeriesMetaList(self):
        return self.getMetaDict()['Series']

    def getDicomSeriesMeta(self, seriesNumber=None, seriesDescription=None):
        if (seriesNumber is None) and (seriesDescription is None):
            raise ValueError("parameter seriesNumber OR seriesDescription must be given")
        allSeries = self.getDicomSeriesMetaList()
        if seriesNumber is not None:
            thisSeries = [i for i in allSeries if i['SeriesNumber']==seriesNumber]
        else:
            seD = seriesDescription.lower()
            thisSeries = [i for i in allSeries if seD in i['SeriesDescription'].lower()]
        return thisSeries

    def getMetaTagsFile(self, suffix=""):
        return os.path.join(self.getMetaDir(), f"{self.subjID}Tags{suffix}.json")

    def setTagValue(self, tag, value, suffix=""):
        self.updateMetaFile({tag:value}, suffix)

    def getTagValue(self, tagName, ifNotFound='Unknown'): # FIXME is this done correctly
        return self.getMetaDict().get(tagName, ifNotFound)

    def getMetaDict(self, suffix=""):
        """Get meta json file as dictionary

        Args:
            suffix (str, optional): Suffix of json file. Defaults to "".

        Returns:
            dict: Meta json file 
        """
        ff = self.getMetaTagsFile(suffix)
        dd = {}
        if os.path.isfile(ff):
            dd = spydcm.dcmTools.parseJsonToDictionary(ff)
        return dd

    def getMetaTagValue(self, tag, NOT_FOUND=None, metaSuffix=""):
        """Get specific tag from meta json file

        Args:
            tag (str): Name of tag to return
            NOT_FOUND (ANY, optional): A default value to return if "tag" not found. Defaults to None.
            metaSuffix (str, optional): Suffix of json file. Defaults to "".

        Raises:
            e: OSError if meta json file not found

        Returns:
            ANY: tag value from json file
        """
        try:
            return self.getMetaDict(metaSuffix).get(tag, NOT_FOUND)
        except OSError as e:
            if NOT_FOUND is not None:
                return NOT_FOUND
            else:
                raise e

    def updateMetaFile(self, metaDict, metasuffix=""):
        """Update the meta json file

        Args:
            metaDict (dict): dictionary with key value pairs to update
            metasuffix (str, optional): Suffix of json file. Defaults to "".
        """
        dd = self.getMetaDict(metasuffix)
        dd.update(metaDict)
        spydcm.dcmTools.writeDictionaryToJSON(self.getMetaTagsFile(metasuffix), dd)
        self.logger.info('updateMetaFile')

    def buildDicomMeta(self):
        """Builds a JSON file comprised of DICOM tags and some derived values. 
        All data is taken from DICOM files - StudyDate, PatientID, MagneticFieldStrength etc
        A 'Series' tag is populated with a list of all series with series information (same as found in ScanSeriesInfo.csv)

        NOTE: miresearch expects one study (scanner exam instance) per subjectID. 
        There are occasions where multiple studies occur but should be treated as one study. 
        E.g.: the subject got off the table and then resummed the study later. 
        miresearch will account for this by recording tags from the first found 'study' at the study level and 
        from ALL found series to populate the list of series. 
        """
        # this uses pydicom - so tag names are different.
        ddFull = {'SubjectID': self.subjID, 'SubjN': self._subjN, 'Series': []}
        dcmStudies = spydcm.dcmTK.ListOfDicomStudies.setFromDirectory(self.getDicomsDir(), HIDE_PROGRESSBAR=True)
        try:
            dcmDict = dcmStudies[0].getStudySummaryDict()
            dcmDict.pop('Series') # Get more detailed series information
            ddFull.update(dcmDict)
            # 
            for iDcmStudy in dcmStudies:
                for iSeries in iDcmStudy:
                    serDict = iSeries.getSeriesInfoDict(["SeriesNumber", 
                                                                "SeriesDescription", 
                                                                "StudyDate", 
                                                                "AcquisitionTime",
                                                                "InPlanePhaseEncodingDirection", 
                                                                "PixelBandwidth"])
                    serDict['DicomFileName'] = iSeries.getDicomFullFileName().replace(self.getTopDir(), "")
                    ddFull['Series'].append(serDict)
        except IndexError:
            pass # Found no Dicoms
        self.updateMetaFile(ddFull)

    def countNumberOfDicoms(self):
        return mi_utils.countFilesInDir(self.getDicomsDir())
    
    def getDicomSeriesDir_Description(self, seriesDescription):
        dd = self.getSeriesNumbersMatchingDescriptionStr(seriesDescription)
        seNs = dd.keys()
        seN = min(seNs)
        return self.getDicomSeriesDir(seN)
    
    def getDicomSeriesDir(self, seriesNum, seriesUID=None):
        dcmStudies = spydcm.dcmTK.ListOfDicomStudies.setFromDirectory(self.getDicomsDir(), ONE_FILE_PER_DIR=True, HIDE_PROGRESSBAR=True)
        if seriesUID is not None:
            for dcmStudy in dcmStudies:
                dcmSeries = dcmStudy.getSeriesByUID()
                if dcmSeries is not None:
                    break
            if dcmSeries is None:
                raise ValueError(f"## ERROR: Series with UID: {seriesUID} NOT FOUND")
        else:
            for dcmStudy in dcmStudies:
                dcmSeries = dcmStudy.getSeriesByID(seriesNum)
                if dcmSeries is not None:
                    break
            if dcmSeries is None:
                raise ValueError(f"## ERROR: Series with SE number: {seriesNum} NOT FOUND")
        dirName = dcmSeries.getRootDir()
        return dirName

    def getDicomFile(self, seriesNum, instanceNum=1):
        #FIXME Note - at some point the files were named incorrectly - this has to work around this... Could be better
        # (and the number of leading zeros changed)
        # possible fix - work it out on per subject basis
        dicomf = os.path.join(self.getDicomSeriesDir(seriesNum), 'IM-%04d-%04d.dcm'%(seriesNum, instanceNum))
        if not os.path.isfile(dicomf):
            dicomf = os.path.join(self.getDicomSeriesDir(seriesNum),
                                  'IM-%04d-%04d.dcm' % (1, instanceNum))
        if not os.path.isfile(dicomf):
            dicomf = os.path.join(self.getDicomSeriesDir(seriesNum),
                                  'IM-%05d-%05d.dcm' % (seriesNum, instanceNum))
        return dicomf

    def getDicomFoldersListStr(self, FULL=True, excludeSeNums=None):
        dFolders = []
        dcmStudies = spydcm.dcmTK.ListOfDicomStudies.setFromDirectory(self.getDicomsDir(), ONE_FILE_PER_DIR=True, HIDE_PROGRESSBAR=True)
        for dcmStudy in dcmStudies:
            for iSeries in dcmStudy:
                dFolders.append(iSeries.getRootDir())
        dS = sorted(dFolders, key=spydcm.dcmTools.instanceNumberSortKey)
        if not FULL:
            dS = [os.path.split(i)[1] for i in dS]
            return dS
        if excludeSeNums is None:
            excludeSeNums = []
        seN = []
        for i in dS:
            try:
                seN.append(int(i.split('_')[0][2:]))
            except ValueError:
                pass
        dcmDirList = [self.getDicomSeriesDir(i) for i in seN if i not in excludeSeNums]
        dcmDirList = sorted(dcmDirList, key=spydcm.dcmTools.instanceNumberSortKey)
        return dcmDirList

    def getListOfSeNums(self):
        se = []
        for ff in self.getDicomFoldersListStr(FULL=False):
            try:
                sn = int(ff.split('_')[0].replace('SE',''))
                se.append(sn)
            except ValueError:
                pass
        return se

    def getStudyID(self):
        studyID = self.getMetaTagValue("StudyID")
        if studyID == "0":
            studyID = self.getMetaTagValue("ScannerStudyID")
        return studyID
    
    def getSeriesDescriptionsStr(self):
        return ','.join(self.getDicomFoldersListStr(FULL=False))


    def getStudyDate(self, RETURN_Datetime=False):
        dos = self.getMetaTagValue('StudyDate')
        if RETURN_Datetime:
            spydcm.dcmTools.dbDateToDateTime(dos)
        return dos

    def getInfoStr(self, extraKeys=[]):
        # Return values_list, info_keys:
        #   list of values for info keys (+ age). 
        #   header keys
        infoKeys = ['SubjectID', 'SubjN', 'PatientBirthDate', 'PatientID', 'PatientName', 'PatientSex',
                    'StudyDate', 'StudyDescription', 'StudyInstanceUID', 'StudyID'] + extraKeys
        mm = self.getMetaDict()
        aa = f"{self.getAge():5.2f}"
        nDCM = f"{self.countNumberOfDicoms()}"
        return [mm.get(i, "Unknown") for i in infoKeys]+[aa, nDCM], infoKeys + ['Age', 'TotalDicoms']

    # ------------------------------------------------------------------------------------------
    def anonymise(self, anonName=None):
        self.logger.info(f'Anonymise in place to {anonName}')
        name, firstNames = self.getName_FirstNames()
        anonName = self._checkAnonName(anonName, name, firstNames)
        # anonName = self._checkAnonName(anonName, patName.split("^")[0], "_".join(patName.split("^")[1:]))
        if type(anonName) == str:
            if len(anonName) == 0:  
                anonName = None # Still anonymise, but let program choose the new anonName
        self.logger.info('Anonymise in place')
        spydcm.anonymiseInPlace(self.getDicomsDir(), anonName=anonName)
        self.setIsAnonymised()
        self.buildDicomMeta()

    def _checkAnonName(self, anonName, name="", firstNames=""):
        self.logger.info(f'_checkAnonName args: {anonName}, name={name}, firstnames={firstNames}') # FIXME debug
        if anonName == "SOFT":
            self.setEncodedName(NAME=name, FIRST_NAMES=firstNames)
            return ""
        elif anonName == "HARD":
            self.setEncodedName(NAME='Name-Unknown', FIRST_NAMES='FirstNames-Unknown')
            return ""
        return anonName
    
    def setIsAnonymised(self):
        self.updateMetaFile({"ANONYMISED": True})
    
    def isAnonymised(self):
        return self.getTagValue("ANONYMISED", False)

    def setEncodedName(self, NAME, FIRST_NAMES=""):
        self.logger.info(f"Adding encoded name {NAME} & {FIRST_NAMES} -- {mi_utils.encodeString('Name-Unknown', self.subjID)}") # FIXME THIS IS DEBUG - REMOVE ME
        dd = {'NAME': mi_utils.encodeString(NAME, self.subjID),
              'FIRST_NAMES': mi_utils.encodeString(FIRST_NAMES, self.subjID)}
        self.updateMetaFile(dd)

    def getName(self):
        if self.isAnonymised():
            try:
                return mi_utils.decodeString(self.getTagValue("NAME", None), self.subjID)
            except:
                return self.getTagValue('PatientName', 'Name-Unknown')
        else:
            return self.getTagValue('PatientName', 'Name-Unknown')

    def getName_FirstNames(self):
        if self.isAnonymised():
            try:
                return mi_utils.decodeString(self.getTagValue("NAME", None), self.subjID), \
                    mi_utils.decodeString(self.getTagValue("FIRST_NAMES", None), self.subjID)
            except TypeError:
                pass
            
        name = self.getName()
        self.logger.info(f"got name {name}") # FIXME THIS IS DEBUG - REMOVE ME
        parts = name.split("^")
        if len(parts) == 1:
            return parts[0], ""
        name = parts[0]
        firstNames = "_".join(parts[1:])
        return spydcm.dcmTools.cleanString(name), spydcm.dcmTools.cleanString(firstNames)


    # ------------------------------------------------------------------------------------------
    def getSummary_list(self):
        hh = ["SubjectID","PatientID","Gender","StudyDate","NumberOfSeries","SERIES_DECRIPTIONS"]
        parts = [self.subjID, self.getMetaTagValue('PatientID'), 
                self.getMetaTagValue('PatientSex'), self.getMetaTagValue('StudyDate'), 
                len(self.getMetaTagValue('Series')), self.getSeriesDescriptionsStr()]
        ss = [str(i) for i in parts]
        return hh, ss

    def getAge(self):
        """
        This returns a float, and is slightly wrong in account of leap years.
        This is intentional.
        :return: years - float
        """
        dd = self.getMetaDict()
        try:
            ageStr = dd['PatientAge']
        except KeyError:
            try:
                birth = dd["PatientBirthDate"]
                study = dd["StudyDate"]
                return (spydcm.dcmTools.dbDateToDateTime(study) - spydcm.dcmTools.dbDateToDateTime(birth)).days / 365.0
            except (KeyError, ValueError):
                return np.nan
        age = np.nan
        try:
            age = int(ageStr)
        except ValueError:
            try:
                age = int(ageStr.lower().replace('y', ''))
            except ValueError:
                pass
        return age

    def getGender(self):
        return self.getMetaDict()['PatientSex']
    
    def isMale(self):
        sex = self.getGender()
        return sex.strip().lower() == 'm'

    # ------------------------------------------------------------------------------------------------------------------
    def zipUpSubject(self, outputDirectory, fileName=None, EXCLUDE_RAW=False):
        """Will zip a subject and place in given output directory

        Args:
            outputDirectory (str): path to output directory
            fileName (str, optional): If given then this is zip filename, if not given then use subjID. Defaults to None.
            EXCLUDE_RAW (bool, optional): Set true to exclude RAW data - helpful for sharing. Defaults to False.

        Returns:
            str: the results full archive name
        """
        if fileName is None:
            fileName = self.subjID
        if not fileName.endswith(".zip"):
            fileName += ".zip"
        archive_name = os.path.join(outputDirectory, fileName)
        with ZipFile(archive_name, 'w') as zipf:
            for root, dirs, files in os.walk(self.getTopDir()):
                if EXCLUDE_RAW: # Exclude RAW subdirectory
                    if 'RAW' in dirs:
                        dirs.remove('RAW')
                #
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, self.dataRoot)
                    zipf.write(file_path, arcname=arcname)
        self.logger.info(f'Zipped subject to {archive_name}')
        return archive_name

    # ------------------------------------------------------------------------------------------------------------------
    def getSpydcmDicomStudy(self):
        return spydcm.dcmTK.DicomStudy.setFromDirectory(self.getDicomsDir())
    
    def getSpydcmDicomSeries(self, seNumber):
        dcmdir = self.getDicomSeriesDir(seNumber)
        return spydcm.dcmTK.DicomSeries.setFromDirectory(dcmdir)

# ====================================================================================================
#       LIST OF SUBJECTS CLASS
# ====================================================================================================
class SubjectList(list):
    """
    Container for a list of subjects
    """
    def __init__(self, subjList=[]):
        super().__init__(i for i in subjList)


    @classmethod
    def setByDirectory(cls, dataRoot, subjectPrefix=None, SubjClass=AbstractSubject):
        listOfSubjects = getAllSubjects(dataRoot, subjectPrefix, SubjClass=SubjClass)
        return cls(listOfSubjects)

    @property
    def subjIDs(self):
        return [i.subjID for i in self]
    
    @property
    def subjNs(self):
        return [i.subjN for i in self]

    def __str__(self) -> str:
        return f"{len(self)} subjects of {self[0].subjectPrefix} at {self[0].dataRoot}"

    def reduceToExist(self):
        toRemove = []
        for i in self:
            if not i.exists():
                toRemove.append(i)
        for i in toRemove:
            self.remove(i)

    def reduceToSet(self):
        toRemove = []
        for k1 in range(len(self)):
            if self[k1] in self[k1+1:]:
                toRemove.append(self[k1])
        for i in toRemove:
            self.remove(i)

    def filterSubjectListByDOS(self, dateOfScan_YYYYMMDD, dateEnd_YYYYMMDD=None): #TODO
        """
        Take list, return only those that match DOS or between start and end (inclusive) if dateEnd given
        :param subjList:
        :param dateOfScan_YYYYMMDD: str
        :param dateEnd_YYYYMMDD: str - optional 
        :return:
        """
        filteredMatchList = []
        for iSubj in self:
            iDOS = iSubj.getTagValue('StudyDate')
            try:
                if dateEnd_YYYYMMDD is None:
                    if iDOS == dateOfScan_YYYYMMDD:
                        filteredMatchList.append(iSubj)
                else:
                    if (int(iDOS) >= int(dateOfScan_YYYYMMDD)) and (int(iDOS) <= int(dateEnd_YYYYMMDD)):
                        filteredMatchList.append(iSubj)
            except ValueError: # maybe don't have tag, or wrong format
                continue
        return SubjectList(filteredMatchList)

    def findSubjMatching_SubjN(self, subjN):
        """
        :param studyID (or examID): int
        :return: mi_subject
        """
        for iSubj in self:
            try:
                if int(iSubj._subjN) == subjN:
                    return iSubj
            except ValueError:
                pass
        return None
    

    def findSubjMatchingStudyID(self, studyID):
        """
        :param studyID (or examID): int
        :return: mi_subject
        """
        for iSubj in self:
            try:
                if int(iSubj.getTagValue("StudyID")) == studyID:
                    return iSubj
            except ValueError:
                pass
        return None
    
    def findSubjMatchingStudyUID(self, studyUID):
        for iSubj in self:
            try:
                if iSubj.getTagValue("StudyInstanceUID") == studyUID:
                    return iSubj
            except TypeError:
                pass
        return None

    def findSubjMatchingPatientID(self, patientID, dateOfScan_YYYYMMDD=None):
        """
        :param patientID:
        :param dateOfScan_YYYY_MM_DD: list of ints for DOS to fix ambiguity
        :return: SubjectList
        """
        patientID = str(patientID)
        matchList = SubjectList()
        for iSubj in self:
            try:
                if iSubj.getTagValue("PatientID") == patientID:
                    matchList.append(iSubj)
            except ValueError:
                pass
        if (len(matchList)>1) & (dateOfScan_YYYYMMDD is not None):
            return matchList.filterSubjectListByDOS(dateOfScan_YYYYMMDD)
        return matchList

    def findSubjMatchingName(self, nameStr, dateOfScan_YYYYMMDD=None, decodePassword=None):
        """
        :param nameStr:
        :param dateOfScan_YYYYMMDD: if given will use to filter list matching name
        :return: SubjectList
        """
        nameStr_l = nameStr.lower()
        matchList = SubjectList()
        for iSubj in self:
            iName = iSubj.getTagValue("NAME", mi_utils.UNKNOWN)
            if decodePassword is not None:
                iName = mi_utils.decodeString(iName, decodePassword).lower()
            try:
                if nameStr_l in iName:
                    matchList.append(iSubj)
            except ValueError:
                pass
        if (len(matchList)>1) & (dateOfScan_YYYYMMDD is not None):
            return matchList.filterSubjectListByDOS(dateOfScan_YYYYMMDD)
        return matchList

    def writeSummaryCSV(self, outputFileName_csv, extra_series_tags=[]):
        data, header = [], []
        for k0, isubj in enumerate(self):
            ss, hh = isubj.getInfoStr()
            if k0 == 0:
                header = hh
            for k1, iSeriesTag in enumerate(extra_series_tags):
                seList = isubj.getDicomSeriesMeta(seriesDescription=iSeriesTag)
                for seDict in seList:
                    if k1 == 0:
                        kkS = sorted(seDict.keys())
                    hh2 = [f"{iSeriesTag}_{kk}" for kk in kkS]
                    if k0 == 0:
                        header += hh2
                    ss += [seDict[i] for i in kkS]
            data.append(ss)
        mi_utils.writeCsvFile(data, header, outputFileName_csv)

### ====================================================================================================================
###  Helper functions for subject list
### ====================================================================================================================
def _getAllSubjects(dataRootDir, subjectPrefix=None, SubjClass=AbstractSubject, RETURN_N=False):
    if subjectPrefix is None:
        subjectPrefix = guessSubjectPrefix(dataRootDir)
    allDir = os.listdir(dataRootDir)
    allDir = [i for i in allDir if i.startswith(subjectPrefix)]
    allDir = [i for i in allDir if os.path.isdir(os.path.join(dataRootDir, i))]
    subjObjList = []
    for i in allDir:
        try:
            iSubjObj = SubjClass(i, dataRoot=dataRootDir)
        except ValueError:
            print(f"WARNING: {i} at {dataRootDir} not valid subject")
        if iSubjObj.exists():
            if RETURN_N:
                subjObjList.append(iSubjObj.subjN)
            else:
                subjObjList.append(iSubjObj)
        else:
            print(f"WARNING: {i} at {dataRootDir} not valid subject")
    return sorted(subjObjList)

def getAllSubjects(dataRootDir, subjectPrefix=None, SubjClass=AbstractSubject):
    return _getAllSubjects(dataRootDir, subjectPrefix, SubjClass)

def getAllSubjectsN(dataRootDir, subjectPrefix=None):
    return _getAllSubjects(dataRootDir, subjectPrefix, RETURN_N=True)

def getSubjects(subjectNList, dataRootDir, subjectPrefix=None, SubjClass=AbstractSubject):
    if subjectPrefix is None:
        subjectPrefix = guessSubjectPrefix(dataRootDir)
    subjObjList = [SubjClass(i, dataRoot=dataRootDir) for i in subjectNList]
    subjObjList = [i for i in subjObjList if i.exists()]
    return sorted(subjObjList)

def subjNListToSubjObj(subjNList, dataRoot, subjPrefix, SubjClass=AbstractSubject, CHECK_EXIST=True):
    subjList = SubjectList([SubjClass(iN, dataRoot, subjPrefix) for iN in subjNList])
    if CHECK_EXIST:
        subjList.reduceToExist()
    return subjList

def WriteSubjectStudySummary(dataRootDir, summaryFilePath=None, subjPrefix=None):
    if (summaryFilePath is None) or (len(summaryFilePath) == 0):
        nowStr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        summaryFilePath = os.path.join(dataRootDir, f'Summary_{nowStr}.csv')
    misubjList = SubjectList.setByDirectory(dataRootDir)
    misubjList.writeSummaryCSV(summaryFilePath)

### ====================================================================================================================
def findSubjMatchingDicomStudyUID(dicomDir_OrData, dataRoot, subjPrefix=None):
    try:
        ds = spydcm.returnFirstDicomFound(dicomDir_OrData)
        queryUID = ds.get('StudyInstanceUID', None)
    except TypeError:
        queryUID = dicomDir_OrData.getTag('StudyInstanceUID', ifNotFound=None)
    if queryUID is None: 
        return None
    SubjList = SubjectList.setByDirectory(dataRoot=dataRoot, subjectPrefix=subjPrefix)
    return SubjList.findSubjMatchingStudyUID(queryUID)


### ====================================================================================================================
def splitSubjID(s):
    """Strip a subject ID to prefix and number

    Args:
        s (str): subject ID

    Returns:
        tuple: prefix: str, number: int (if len 3 - then also suffix: str)
    """
    parts = re.split(r'(\d+)', s)  # Split the string on one or more digits
    parts = [part for part in parts if part]  # Filter out empty parts
    if len(parts) >= 3:
        return parts[0], int(parts[1]), ''.join(parts[2:])
    return parts[0], int(parts[1])

def getNumberFromSubjID(subjID):
    return splitSubjID(subjID)[1]

def findZeroPadding(subjID):
    match = re.search(r'\d+', subjID) # first seq of numbers
    if match:
        number = match.group()  # group numbers
        return len(number)# 
    else:
        return 0  # If no number found, return 0

def guessSubjectPrefix(dataRootDir, QUIET=False):
    """Guess the subject prefix by looking for common names in the dataRootDir

    Args:
        dataRootDir (str): path to root directory of subject filesystem database
        QUIET      (bool): Set True to suppress output (default False)

    Returns:
        str: subject prefix string

    Exception:
        mi_utils.SubjPrefixError: is ambiguous
    """
    allDir = [i for i in os.listdir(dataRootDir) if os.path.isdir(os.path.join(dataRootDir, i))]
    allDir_subj = {}
    for i in allDir:
        try:
            prefix_N_suffix = splitSubjID(i)
            prefix = prefix_N_suffix[0]
            N = prefix_N_suffix[1]
        except (ValueError, IndexError): 
            continue # directory not correct format - could not split to integer
        allDir_subj.setdefault(prefix, []).append(N)
    options = list(allDir_subj.keys())
    if len(options) == 0:
        raise mi_utils.SubjPrefixError("Error guessing subject prefix - ambiguous - please provide")
    counts = [len(allDir_subj[i]) for i in options]
    maxCount = np.argmax(counts)
    if options.count(options[maxCount]) != 1:
        raise mi_utils.SubjPrefixError("Error guessing subject prefix - ambiguous - please provide")
    res = options[maxCount]
    if not QUIET:
        print(f"subjectPrefix determined from {dataRootDir} = {res}")
    return res

### ====================================================================================================================
###  Helper functions for building new or adding to subjects
### ====================================================================================================================
def buildSubjectID(subjN, subjectPrefix, padZeros=mi_utils.MIResearch_config.default_pad_zeros, suffix=''):
    if subjN is None:
        return subjectPrefix
    return f"{subjectPrefix}{subjN:0{padZeros}d}{suffix}"

def getNextSubjN(dataRootDir, subjectPrefix=None):
    if subjectPrefix is None:
        subjectPrefix = guessSubjectPrefix(dataRootDir)
    allNums = [getNumberFromSubjID(i) for i in os.listdir(dataRootDir) if (os.path.isdir(os.path.join(dataRootDir, i)) and  i.startswith(subjectPrefix))]
    try:
        return max(allNums)+1
    except ValueError:
        return 1

def doesSubjectExist(subjN, dataRootDir, subjectPrefix=None, padZeros=mi_utils.MIResearch_config.default_pad_zeros, suffix=""):
    if subjectPrefix is None:
        subjectPrefix = guessSubjectPrefix(dataRootDir)
    return os.path.isdir(os.path.join(dataRootDir, buildSubjectID(subjN, subjectPrefix, padZeros=padZeros, suffix=suffix)))

def getNextSubjID(dataRootDir, subjectPrefix=None):
    if subjectPrefix is None:
        subjectPrefix = guessSubjectPrefix(dataRootDir)
    return buildSubjectID(getNextSubjN(dataRootDir, subjectPrefix), subjectPrefix)

def _createSubjectHelper(dicomDir_orData, SubjClass, subjNumber, dataRoot, subjPrefix, anonName, QUIET, FORCE_NEW_SUBJ=False):
    if FORCE_NEW_SUBJ:
        newSubj = None
    else:
        # Check if a subject already exists with dicom data matching input
        newSubj = findSubjMatchingDicomStudyUID(dicomDir_orData, dataRoot, subjPrefix)
    if newSubj is not None:
        # Subject exists - so check nothing conflicting from inputs
        if subjNumber is not None:
            if subjNumber != newSubj.subjN:
                raise ValueError(f"You supplied subject number {subjNumber} but a different subject matching your input dicom study exists at {newSubj.subjN}")
        print(f"Found existing subject {newSubj.subjID} at {dataRoot} - adding to")
    
    # If no subject exists matching the inputs - define a new subject (increment subjN from current in root directory)
    if newSubj is None: 
        subjNumber = _subjNumberHelper(dataRoot=dataRoot, subjNumber=subjNumber, subjPrefix=subjPrefix)
        newSubj = SubjClass(subjNumber, dataRoot, subjectPrefix=subjPrefix)
    newSubj.QUIET = QUIET

    # Now have a subject - either newly created or existing and matching dicom data - load dicoms to subject:
    if os.path.isdir(dicomDir_orData):
        newSubj.loadDicomsToSubject(dicomDir_orData, anonName=anonName, HIDE_PROGRESSBAR=QUIET)
    else:
        newSubj.loadSpydcmStudyToSubject(dicomDir_orData, anonName=anonName)
    #
    return newSubj

def _createNewSubject_Compressed(compressedFile, dataRoot, SubjClass=AbstractSubject, 
                                subjNumber=None, subjPrefix=None, anonName=None, QUIET=False):
    if compressedFile.endswith('zip'):
        listOfSubjects = spydcm.dcmTK.ListOfDicomStudies.setFromZip(compressedFile, HIDE_PROGRESSBAR=QUIET)
    elif compressedFile.endswith('tar') or compressedFile.endswith('tar.gz'):
        listOfSubjects = spydcm.dcmTK.ListOfDicomStudies.setFromTar(compressedFile, HIDE_PROGRESSBAR=QUIET)
    else: 
        raise ValueError("Currently only supporting .zip, .tar and .tar.gz compressed files")
    if len(listOfSubjects) > 1:
        if subjNumber is not None:
            raise ValueError(f"More than one study in {compressedFile} - can not supply subjNumber")
    newSubjList = []
    for i in listOfSubjects:
        newSubj = _createSubjectHelper(i, SubjClass, subjNumber=subjNumber, dataRoot=dataRoot, 
                                        subjPrefix=subjPrefix, anonName=anonName, QUIET=QUIET)
        newSubjList.append(newSubj)
    if len(newSubjList) == 1:
        return newSubjList[0]
    return newSubjList

def _subjNumberHelper(dataRoot, subjNumber, subjPrefix):
    if subjNumber is None:
        subjNumber = getNextSubjN(dataRoot, subjPrefix)
    else:
        if doesSubjectExist(subjNumber, dataRoot, subjPrefix):
            raise ValueError("Subject already exists - use loadDicomsToSubject method to add data to existing subject.")
    return subjNumber

def _createNew_OrAddTo_Subject(dicomDirToLoad, dataRoot, SubjClass=AbstractSubject, 
                     subjNumber=None, subjPrefix=None, anonName=None, QUIET=False, IGNORE_UIDS=False):
    if not os.path.isdir(dicomDirToLoad):
        if os.path.isfile(dicomDirToLoad):
            newSubj = _createNewSubject_Compressed(dicomDirToLoad, dataRoot, SubjClass=SubjClass, subjNumber=subjNumber, 
                                        subjPrefix=subjPrefix, anonName=anonName, QUIET=QUIET)
            return newSubj
        raise IOError(" Load dir does not exist")
    if spydcm.returnFirstDicomFound(dicomDirToLoad) is None:
        raise IOError(f"Can not find valid dicoms under {dicomDirToLoad}")
    if not os.path.isdir(dataRoot):
        raise IOError(f" Destination does not exist: {dataRoot}")
    newSubj = _createSubjectHelper(dicomDirToLoad, SubjClass, subjNumber=subjNumber, dataRoot=dataRoot, 
                                    subjPrefix=subjPrefix, anonName=anonName, QUIET=QUIET, 
                                    FORCE_NEW_SUBJ=IGNORE_UIDS)
    #
    return newSubj

def _createNew_OrAddTo_Subjects_Multi(multiDicomDirToLoad, dataRoot, 
                                       SubjClass=AbstractSubject, subjPrefix=None, 
                                       IGNORE_UIDS=False, QUIET=False):
    if not os.path.isdir(multiDicomDirToLoad):
        raise IOError(" Load dir does not exist")
    dirsToLoad = [os.path.join(multiDicomDirToLoad, i) for i in os.listdir(multiDicomDirToLoad)]
    dirsToLoad = [i for i in dirsToLoad if os.path.isdir(i)]
    dirsToLoad_checked = []
    if not os.path.isdir(dataRoot):
        raise IOError("Destination does not exist")
    for iDir in dirsToLoad:
        if spydcm.returnFirstDicomFound(iDir) is not None:
            dirsToLoad_checked.append(iDir)
    if len(dirsToLoad_checked) == 0:
        raise IOError(f"Can not find valid dicoms under {multiDicomDirToLoad}")
    newSubjsList = []
    for iDir in dirsToLoad_checked:
        newSubjsList.append(_createNew_OrAddTo_Subject(iDir, 
                                             dataRoot=dataRoot,
                                             SubjClass=SubjClass,
                                             subjPrefix=subjPrefix,
                                             QUIET=QUIET,
                                             IGNORE_UIDS=IGNORE_UIDS))
    return newSubjsList

### ====================================================================================================================
def createNew_OrAddTo_Subject(loadDirectory, dataRoot, SubjClass=AbstractSubject, 
                           subjNumber=None, subjPrefix=None, anonName=None, 
                           LOAD_MULTI=False, IGNORE_UIDS=False, QUIET=False):
    """Used to create a new subject (or add data to already existing subject) from an input directory (or compressed file).
    Current compressed file tpyes supported: zip, tar, tar.gz

    Args:
        loadDirectory (str): the directory from which data to be loaded
        dataRoot (str): the root directory where subjects are stored
        SubjClass (subclass of AbstractClass, optional): subclass of AbstractClass. Defaults to AbstractSubject.
        subjNumber (int, optional): subject number to create or load to. Will take next available number if none given. Defaults to None.
        subjPrefix (str, optional): the subject prefix. If not given will attempt to guess from dataRoot. Defaults to None.
        anonName (str, optional): An anonymis name to give to this subject. Defaults to None.
        LOAD_MULTI (bool, optional): If true then each sub-directory in "loadDirectory" will be used to load a new subject. Defaults to False.
        IGNORE_UIDS (bool, optional): If true then ignore dicom UIDs and each sub-directory in "loadDirectory" will DEFINITLY be a new subject. Defaults to False.
        QUIET (bool, optional): If true will supress output. Defaults to False.

    Raises:
        ValueError: If incompatible arguments given (can not give subjNumber if LOAD_MULTI is given)

    Returns:
        list: list of Subject Objects added to or created
    """
    if LOAD_MULTI and ((subjNumber is not None) or (anonName is not None)):
        raise ValueError("Can not pass subjNumber if LOAD_MULTI set True")
    if LOAD_MULTI:
        return SubjectList(_createNew_OrAddTo_Subjects_Multi(loadDirectory, 
                                       dataRoot=dataRoot, 
                                       SubjClass=SubjClass, 
                                       subjPrefix=subjPrefix, 
                                       IGNORE_UIDS=IGNORE_UIDS,
                                       QUIET=QUIET))
    else:
        return SubjectList([_createNew_OrAddTo_Subject(loadDirectory, 
                                dataRoot=dataRoot,
                                SubjClass=SubjClass,
                                subjNumber=subjNumber,
                                subjPrefix=subjPrefix, 
                                anonName=anonName, 
                                QUIET=QUIET)])
    
### ====================================================================================================================
### ====================================================================================================================