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
    return Kink     #in radian

def OpeningAngle(SX1, SY1, SX2, SY2):   #slopes of two track
    spcdiff2 = (SX1 - SX2)**2 + (SY1 - SY2)**2
    OAngle = r.TMath.Sqrt(spcdiff2)
    return OAngle

def ImpactParameter(trackPos, trackMom, targetPos):
    t = 0.
    for i in range(3):
        t += trackMom[i]/trackMom[3]*(targetPos[i]-trackPos[i])
    dist = 0.
    for j in range(3):
        dist += (targetPos[i]-trackPos[i]-t*trackMom[i]/trackMom[3])**2
    IP = r.TMath.Sqrt(dist)
    return IP     #in cm

def ImpactParameterV2(CPos, CDauPos, SlopeX, SlopeY):
    EPX = CDauPos[0]+(CDauPos[2]-CPos[2])*SlopeX
    EPY = CDauPos[1]+(CDauPos[2]-CPos[2])*SlopeY
    IP = r.TMath.Sqrt((CPos[0]-EPX)**2 + (CPos[1]-EPY)**2)
    return IP   #in cm

def Multiplicity(PdgArr, RArr):
    Mult = 0
    for i in range(len(PdgArr)):
      if PdgArr[i] not in RArr:
        Mult += 1
    return Mult
