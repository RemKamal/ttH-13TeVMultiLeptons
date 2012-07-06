#!/usr/bin/env python
import math
# import the environment 
from PlotEnv import *

# import the plots you want
from myPlots import *

# import the root libraries
# with this kind of import
# you won't need to prefix your root objects with ROOT

from ROOT import *

# this is the function that is called
# when you type ./drawPlots.py
# there are some optional arguments

def main ():
	
    lepselection = []
    jetselection = []
    lepselection.append("TwoMuon")
    lepselection.append("TwoEle")
    lepselection.append("MuonEle")
    jetselection.append("eq1t")
    jetselection.append("eq2jeq2t")
    jetselection.append("ge3t")

    Outputs = {}
    numBins = 1
        
    parser = OptionParser()
    parser.add_option('-L', '--Lumi', dest='lumi', default=5.0, help='integrated lumi')
    parser.add_option('-b', dest="batch", action='store_true', default=false)
    
    (options, args) = parser.parse_args()
    for jet in jetselection:
        Outputs[jet] = {}
        for lep in lepselection:
            # This function is defined in
            # myPlots.py
            # it returns the plots you want

            AndrewPlotGroup = getMyPlotsAndrewNorm(lep,jet)
        
            myLumi = AndrewPlotGroup.lumi
            AndrewPlotGroup.lumi = myLumi*1e3

            print "Using lumi %f" % myLumi
            
            pg = AndrewPlotGroup

            # Set the style for your plots

            ROOT.gROOT.SetStyle("Plain")
            ROOT.gStyle.SetOptStat(0)
            ROOT.gStyle.SetPadLeftMargin(0.15)
            ROOT.gStyle.SetPadRightMargin(0.07)
            ROOT.gStyle.SetPadTopMargin(0.07)
            ROOT.gStyle.SetPadBottomMargin(0.1)
            ROOT.gStyle.SetOptStat(0)
            ROOT.gStyle.SetTitleOffset(1.4, "y")

            # This is the good stuff
            # draw the plots
            # Arguments are
            #   1. What distribution?
            #   2. Which plots?
            #   3. Title for the plots
            #   4,5,6. New binning, just like TH1F arguments (bins, xMin, xMax)
            #   7. Lepton selection
            #   8. make "plots" or "print" table

            # Echo the current config
            
            pg.show()

#            Outputs[jet][lep] = drawStackPlot("numJets", pg, "numJets", 1, 0, 50, lep, "print")
#            Outputs[jet][lep] = drawStackPlot("Ht", pg, "Ht", 1, 0, 50000, lep, "print")
            Outputs[jet][lep] = drawStackPlot("CFMlpANN_ge3t", pg, "CFMlpANN_ge3t", 1, 0, 1, lep, "print")




    print ''
    print '\multirow{4}{*}{$\geq$2 jets + 1 tag} & $\mu\mu $ & '+str(round(Outputs["eq1t"]["TwoMuon"][0],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][1],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][2],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][3],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][4],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][5],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][6],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][7],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][8],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][9],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][10],2))+' $\pm$ '+str(round(Outputs["eq1t"]["TwoMuon"][11],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][12],0))+'  \\'+'\\'  
    print ' & $ee$ & '+str(round(Outputs["eq1t"]["TwoEle"][0],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][1],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][2],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][3],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][4],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][5],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][6],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][7],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][8],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][9],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][10],2))+' $\pm$ '+str(round(Outputs["eq1t"]["TwoEle"][11],2))+' & '+str(round(Outputs["eq1t"]["TwoEle"][12],0))+'  \\'+'\\'
    print ' & $\mu e$ & '+str(round(Outputs["eq1t"]["MuonEle"][0],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][1],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][2],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][3],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][4],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][5],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][6],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][7],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][8],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][9],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][10],2))+' $\pm$ '+str(round(Outputs["eq1t"]["MuonEle"][11],2))+' & '+str(round(Outputs["eq1t"]["MuonEle"][12],0))+'  \\'+'\\'
    print ' & tot & '+str(round(Outputs["eq1t"]["TwoMuon"][0]+Outputs["eq1t"]["TwoEle"][0]+Outputs["eq1t"]["MuonEle"][0],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][1]+Outputs["eq1t"]["TwoEle"][1]+Outputs["eq1t"]["MuonEle"][1],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][2]+Outputs["eq1t"]["TwoEle"][2]+Outputs["eq1t"]["MuonEle"][2],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][3]+Outputs["eq1t"]["TwoEle"][3]+Outputs["eq1t"]["MuonEle"][3],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][4]+Outputs["eq1t"]["TwoEle"][4]+Outputs["eq1t"]["MuonEle"][4],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][5]+Outputs["eq1t"]["TwoEle"][5]+Outputs["eq1t"]["MuonEle"][5],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][6]+Outputs["eq1t"]["TwoEle"][6]+Outputs["eq1t"]["MuonEle"][6],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][7]+Outputs["eq1t"]["TwoEle"][7]+Outputs["eq1t"]["MuonEle"][7],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][8]+Outputs["eq1t"]["TwoEle"][8]+Outputs["eq1t"]["MuonEle"][8],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][9]+Outputs["eq1t"]["TwoEle"][9]+Outputs["eq1t"]["MuonEle"][9],2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][10]+Outputs["eq1t"]["TwoEle"][10]+Outputs["eq1t"]["MuonEle"][10],2))+' $\pm$ '+str(round(sqrt(pow(Outputs["eq1t"]["TwoMuon"][11],2)+pow(Outputs["eq1t"]["TwoEle"][11],2)+pow(Outputs["eq1t"]["MuonEle"][11],2)),2))+' & '+str(round(Outputs["eq1t"]["TwoMuon"][12]+Outputs["eq1t"]["TwoEle"][12]+Outputs["eq1t"]["MuonEle"][12],0))+'  \\'+'\\ \hline'
    print '\multirow{4}{*}{      2 jets + 2 tags} & $\mu\mu $ & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][0],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][1],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][2],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][3],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][4],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][5],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][6],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][7],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][8],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][9],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][10],2))+' $\pm$ '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][11],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][12],0))+'  \\'+'\\'  
    print ' & $ee$ & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][0],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][1],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][2],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][3],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][4],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][5],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][6],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][7],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][8],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][9],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][10],2))+' $\pm$ '+str(round(Outputs["eq2jeq2t"]["TwoEle"][11],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoEle"][12],0))+'  \\'+'\\'
    print ' & $\mu e$ & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][0],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][1],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][2],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][3],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][4],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][5],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][6],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][7],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][8],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][9],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][10],2))+' $\pm$ '+str(round(Outputs["eq2jeq2t"]["MuonEle"][11],2))+' & '+str(round(Outputs["eq2jeq2t"]["MuonEle"][12],0))+'  \\'+'\\'
    print ' & tot & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][0]+Outputs["eq2jeq2t"]["TwoEle"][0]+Outputs["eq2jeq2t"]["MuonEle"][0],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][1]+Outputs["eq2jeq2t"]["TwoEle"][1]+Outputs["eq2jeq2t"]["MuonEle"][1],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][2]+Outputs["eq2jeq2t"]["TwoEle"][2]+Outputs["eq2jeq2t"]["MuonEle"][2],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][3]+Outputs["eq2jeq2t"]["TwoEle"][3]+Outputs["eq2jeq2t"]["MuonEle"][3],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][4]+Outputs["eq2jeq2t"]["TwoEle"][4]+Outputs["eq2jeq2t"]["MuonEle"][4],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][5]+Outputs["eq2jeq2t"]["TwoEle"][5]+Outputs["eq2jeq2t"]["MuonEle"][5],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][6]+Outputs["eq2jeq2t"]["TwoEle"][6]+Outputs["eq2jeq2t"]["MuonEle"][6],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][7]+Outputs["eq2jeq2t"]["TwoEle"][7]+Outputs["eq2jeq2t"]["MuonEle"][7],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][8]+Outputs["eq2jeq2t"]["TwoEle"][8]+Outputs["eq2jeq2t"]["MuonEle"][8],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][9]+Outputs["eq2jeq2t"]["TwoEle"][9]+Outputs["eq2jeq2t"]["MuonEle"][9],2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][10]+Outputs["eq2jeq2t"]["TwoEle"][10]+Outputs["eq2jeq2t"]["MuonEle"][10],2))+' $\pm$ '+str(round(sqrt(pow(Outputs["eq2jeq2t"]["TwoMuon"][11],2)+pow(Outputs["eq2jeq2t"]["TwoEle"][11],2)+pow(Outputs["eq2jeq2t"]["MuonEle"][11],2)),2))+' & '+str(round(Outputs["eq2jeq2t"]["TwoMuon"][12]+Outputs["eq2jeq2t"]["TwoEle"][12]+Outputs["eq2jeq2t"]["MuonEle"][12],0))+'  \\'+'\\ \hline'
    print '\multirow{4}{*}{$\geq$3 tags         } & $\mu\mu $ & '+str(round(Outputs["ge3t"]["TwoMuon"][0],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][1],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][2],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][3],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][4],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][5],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][6],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][7],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][8],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][9],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][10],2))+' $\pm$ '+str(round(Outputs["ge3t"]["TwoMuon"][11],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][12],0))+'  \\'+'\\'  
    print ' & $ee$ & '+str(round(Outputs["ge3t"]["TwoEle"][0],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][1],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][2],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][3],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][4],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][5],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][6],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][7],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][8],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][9],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][10],2))+' $\pm$ '+str(round(Outputs["ge3t"]["TwoEle"][11],2))+' & '+str(round(Outputs["ge3t"]["TwoEle"][12],0))+'  \\'+'\\'
    print ' & $\mu e$ & '+str(round(Outputs["ge3t"]["MuonEle"][0],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][1],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][2],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][3],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][4],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][5],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][6],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][7],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][8],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][9],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][10],2))+' $\pm$ '+str(round(Outputs["ge3t"]["MuonEle"][11],2))+' & '+str(round(Outputs["ge3t"]["MuonEle"][12],0))+'  \\'+'\\'
    print ' & tot & '+str(round(Outputs["ge3t"]["TwoMuon"][0]+Outputs["ge3t"]["TwoEle"][0]+Outputs["ge3t"]["MuonEle"][0],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][1]+Outputs["ge3t"]["TwoEle"][1]+Outputs["ge3t"]["MuonEle"][1],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][2]+Outputs["ge3t"]["TwoEle"][2]+Outputs["ge3t"]["MuonEle"][2],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][3]+Outputs["ge3t"]["TwoEle"][3]+Outputs["ge3t"]["MuonEle"][3],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][4]+Outputs["ge3t"]["TwoEle"][4]+Outputs["ge3t"]["MuonEle"][4],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][5]+Outputs["ge3t"]["TwoEle"][5]+Outputs["ge3t"]["MuonEle"][5],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][6]+Outputs["ge3t"]["TwoEle"][6]+Outputs["ge3t"]["MuonEle"][6],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][7]+Outputs["ge3t"]["TwoEle"][7]+Outputs["ge3t"]["MuonEle"][7],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][8]+Outputs["ge3t"]["TwoEle"][8]+Outputs["ge3t"]["MuonEle"][8],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][9]+Outputs["ge3t"]["TwoEle"][9]+Outputs["ge3t"]["MuonEle"][9],2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][10]+Outputs["ge3t"]["TwoEle"][10]+Outputs["ge3t"]["MuonEle"][10],2))+' $\pm$ '+str(round(sqrt(pow(Outputs["ge3t"]["TwoMuon"][11],2)+pow(Outputs["ge3t"]["TwoEle"][11],2)+pow(Outputs["ge3t"]["MuonEle"][11],2)),2))+' & '+str(round(Outputs["ge3t"]["TwoMuon"][12]+Outputs["ge3t"]["TwoEle"][12]+Outputs["ge3t"]["MuonEle"][12],0))+'  \\'+'\\ \hline'

    return
	
# This allows you to run at the command line	
# tells you to call the main function defined above
if __name__ == '__main__':
	main()

