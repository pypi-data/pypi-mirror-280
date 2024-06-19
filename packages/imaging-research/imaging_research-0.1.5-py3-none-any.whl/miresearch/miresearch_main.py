# -*- coding: utf-8 -*-

"""Module that exposes the routines and utilities making up MIRESEARCH
"""

import os
import sys
import argparse

from miresearch import mi_utils
from miresearch import mi_subject
from miresearch import miresearch_watchdog
from miresearch.mi_config import MIResearch_config


### ====================================================================================================================
#          ARGUEMTENT PARSING AND ACTIONS 
### ====================================================================================================================
# Override error to show help on argparse error (missing required argument etc)
class MiResearchParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

ParentAP = MiResearchParser(epilog="Written Fraser M. Callaghan. MRZentrum, University Children's Hospital Zurich")

groupM = ParentAP.add_argument_group('Management Parameters')
groupM.add_argument('-config', dest='configFile', help='Path to configuration file to use.', type=str, default=None)
groupM.add_argument('-FORCE', dest='FORCE', help='force action - use with caution',
                        action='store_true')
groupM.add_argument('-QUIET', dest='QUIET', help='Suppress progress bars and logging to terminal',
                        action='store_true')
groupM.add_argument('-INFO', dest='INFO', help='Provide setup (configuration) info and exit.',
                        action='store_true')
groupM.add_argument('-DEBUG', dest='DEBUG', help='Run in DEBUG mode (save intermediate steps, increase log output)',
                        action='store_true')

groupS = ParentAP.add_argument_group('Subject Definition')
groupS.add_argument('-s', dest='subjNList', help='Subject number(s)', nargs="*", type=int, default=[])
groupS.add_argument('-sA', dest='AllSubjs', help='All subjects', action='store_true')
groupS.add_argument('-sf', dest='subjNListFile', help='Subject numbers in file', type=str, default=None)
groupS.add_argument('-sR', dest='subjRange', help='Subject range', nargs=2, type=int, default=[])
groupS.add_argument('-y', dest='dataRoot', 
                    help='Path of root data directory (where subjects are stored) [default None -> may be set in config file]', 
                    type=str, default=None)
groupS.add_argument('-sPrefix', dest='subjPrefix', 
                    help='Subject prefix [default None -> will get from config file OR dataRoot]', 
                    type=str, default=None)
groupS.add_argument('-sSuffix', dest='subjSuffix', 
                    help='Subject suffix [default ""]', 
                    type=str, default="")
groupS.add_argument('-anonName', dest='anonName', 
                    help='Set to anonymise newly loaded subject. Set to true to use for WatchDirectory. [default None]', 
                    type=str, default=None)
    
groupA = ParentAP.add_argument_group('Actions')
# LOADING
groupA.add_argument('-Load', dest='loadPath', 
                    help='Path to load dicoms from (file / directory / tar / tar.gz / zip)', 
                    type=str, default=None)
groupA.add_argument('-LOAD_MULTI', dest='LoadMulti', 
                    help='Combine with "Load": Load new subject for each subdirectory under loadPath', 
                    action='store_true')
groupA.add_argument('-LOAD_MULTI_FORCE', dest='LoadMultiForce', 
                    help='Combine with "Load": Force to ignore studyUIDs and load new ID per subdirectory', 
                    action='store_true')

# SUBJECT LEVEL
groupA.add_argument('-RunPost', dest='subjRunPost', 
                    help='Run post load pipeline', 
                    action='store_true')
groupA.add_argument('-SubjInfo', dest='subjInfo', 
                    help='Print info for each subject', 
                    action='store_true')

# GROUP ACTIONS
groupA.add_argument('-SummaryCSV', dest='SummaryCSV', 
                    help='Write summary CSV file (give output file name)', 
                    type=str, nargs="*", default=None)

# WATCH DIRECTORY
groupA.add_argument('-WatchDirectory', dest='WatchDirectory', 
                    help='Will watch given directory for new data and load as new study', 
                    type=str, default=None)


### ====================================================================================================================
#           CHECK ARGS
### ====================================================================================================================

def setNList(args):
    if args.AllSubjs:
        args.subjNList = mi_subject.getAllSubjectsN(args.dataRoot, args.subjPrefix)
    else:
        if len(args.subjRange) == 2:
            args.subjNList = args.subjNList+list(range(args.subjRange[0], args.subjRange[1]))
        if args.subjNListFile:
            args.subjNList = args.subjNList+mi_utils.subjFileToSubjN(args.subjNListFile)
    # args.subjNList = sorted(list(set(args.subjNList)))

def checkArgs(args):
    # 
    if args.configFile: MIResearch_config.runconfigParser(args.configFile)
    if args.INFO:
        MIResearch_config.printInfo()
        sys.exit(1)
    #
    if args.dataRoot is not None:
        args.dataRoot = os.path.abspath(args.dataRoot)
    else:
        args.dataRoot = MIResearch_config.data_root_dir
    if args.subjPrefix is None:
        args.subjPrefix = MIResearch_config.subject_prefix
    if args.anonName is None:
        args.anonName = MIResearch_config.anon_level
    if not args.QUIET:
        print(f'Running MIRESEARCH with dataRoot {args.dataRoot}')
    if args.loadPath is not None:
        args.loadPath = os.path.abspath(args.loadPath)
    if args.LoadMultiForce:
        args.LoadMulti = True
    
    MISubjClass = mi_subject.AbstractSubject
    if MIResearch_config.class_obj:
        MISubjClass = MIResearch_config.class_obj
    args.MISubjClass = MISubjClass
    ## -------------
    setNList(args=args)

### ====================================================================================================================
#           RUN ACTIONS
### ====================================================================================================================
def runActions(args, extra_runActions=None):

    # --- LOAD ---
    if args.loadPath is not None:
        if len(args.subjNList) == 0:
            args.subjNList = [None]
        if not args.QUIET:
            print(f'Running MIRESEARCH with loadPath {args.loadPath}')
        mi_subject.createNew_OrAddTo_Subject(loadDirectory=args.loadPath,
                                             dataRoot=args.dataRoot,
                                             subjPrefix=args.subjPrefix,
                                             subjNumber=args.subjNList[0],
                                             anonName=args.anonName,
                                             LOAD_MULTI=args.LoadMulti,
                                             SubjClass=args.MISubjClass,
                                             IGNORE_UIDS=args.LoadMultiForce,
                                             QUIET=args.QUIET)
    # SUBJECT LEVEL actions
    elif len(args.subjNList) > 0:
        if args.DEBUG:
            print(f"SubjList provided is: {args.subjNList}")
        subjList = mi_subject.SubjectList([args.MISubjClass(sn, args.dataRoot, args.subjPrefix, suffix=args.subjSuffix) for sn in args.subjNList])
        # --- ANONYMISE ---
        if args.anonName is not None:
            for iSubj in subjList:
                if iSubj.exists():
                    if not args.QUIET:
                        print(f"Anonymise: {iSubj.subjID}...")
                    iSubj.anonymise(args.anonName)

        # --- POST LOAD PIPELINE ---
        elif args.subjRunPost:
            for iSubj in subjList:
                if iSubj.exists():
                    if not args.QUIET:
                        print(f"Post load pipeline: {iSubj.subjID}...")
                    iSubj.runPostLoadPipeLine()

        # --- PRINT INFO ---
        elif args.subjInfo:
            for iSubj in subjList:
                if iSubj.exists():
                    if args.DEBUG:
                        print(f"Info: {iSubj.subjID}...")
                    iSubj.info()

        # === SUBJECT GROUP ACTIONS ===
        # --- SummaryCSV ---
        elif args.SummaryCSV is not None:
            if not args.QUIET:
                print(f"Info: writting summary for {len(args.subjNList)} subjects at {args.dataRoot} to {args.SummaryCSV[0]}")
                if len(args.SummaryCSV) > 1:
                    print(f"  With tags: {args.SummaryCSV[1:]}")
            subjList.writeSummaryCSV(args.SummaryCSV[0], extra_series_tags=args.SummaryCSV[1:])


    ## WATCH DIRECTORY ##
    elif args.WatchDirectory is not None:

        MIWatcher = miresearch_watchdog.MIResearch_WatchDog(args.WatchDirectory,
                                        args.dataRoot,
                                        args.subjPrefix,
                                        SubjClass=args.MISubjClass,
                                        TO_ANONYMISE=(args.anonName is not None),
                                        DEBUG=args.DEBUG)
        MIWatcher.run()

    if extra_runActions is not None:
        extra_runActions(args)

### ====================================================================================================================
### ====================================================================================================================
# S T A R T
def main(extra_runActions=None):
    arguments = ParentAP.parse_args()
    checkArgs(arguments) # Will substitute from config files if can
    runActions(arguments, extra_runActions)


if __name__ == '__main__':
    main()