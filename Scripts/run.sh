for i in {0..9}; do
    if [[ -d /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/below/6313076."$i" ]]; then 
        python SingleBuilder.py --work_dir /eos/experiment/ship/user/eelikkaya/NICPStudies/SingleCheck --input_path /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/below/6313076."$i" --geo_file /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/below/6313076.30/geofile_full.conical.Genie-TGeant4.root -n 1 --flavor nu_mu &&
        mv ../SingleCheck/nu_mu.root ../SingleCheck/below_6313076."$i".root &&
        echo $i
   fi
done
