import ROOT as r

def FlightLength(DPos, MPos):
    dist = 0.
    for i in range(3):
        dist += (DPos[i] - MPos[i])**2
    FL = r.TMath.Sqrt(dist)
    return FL

def Slope(Pi, Pz):
    Slope = r.TMath.ATan(Pi/Pz)
    return Slope

def KinkAngle(MSlopeX, MSlopeY, DSlopeX, DSlopeY):
    spcdiff2 = (MSlopeX - DSlopeX)**2 + (MSlopeY - DSlopeY)**2
    Kink = r.TMath.Sqrt(spcdiff2)
    return Kink

def ImpactParameter(trackPos, trackMom, targetPos):
    t = 0.
    for i in range(3):
        t += trackMom[i]/trackMom[3]*(targetPos[i]-trackPos[i])
    dist = 0.
    for j in range(3):
        dist += (targetPos[i]-trackPos[i]-t*trackMom[i]/trackMom[3])**2
    IP = r.TMath.Sqrt(dist)
    return IP
