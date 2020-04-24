for eachF in /eos/experiment/ship/user/eelikkaya/NICPStudies/SingleCheck/* ; do 
    python XCharmAna.py --work_dir /eos/experiment/ship/user/eelikkaya/NICPStudies/SingleCheck --geo_file /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/above/6313075.1/geofile_full.conical.Genie-TGeant4.root --input_file $eachF | grep "Geometry Selection Success" && echo $eachF
done | tee numu_Above100K.out
