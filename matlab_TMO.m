for i = 1:8
    myFolder = strcat('/home/ziyi/Desktop/ImagesDataset1/scene',strcat(int2str(i),'/Multi-Face/HDR/'));
    destination = strcat('/home/ziyi/Desktop/ToneMapped/scene',strcat(int2str(i),'/Multi-Face/AshikhminTMO/'));
    
    filePattern = fullfile(myFolder, '*.hdr');
    jpegFiles = dir(filePattern);

    for k = 1:length(jpegFiles)
      baseFileName = jpegFiles(k).name;
      fullFileName = fullfile(myFolder, baseFileName);
      fprintf(1, 'Now reading %s\n', fullFileName);
      [img] = hdrread(fullFileName);                                                                                  

      [filepath,filename,forma] = fileparts(baseFileName);
      format = '.png';

      %imgOut = BestExposureTMO(img);
      %imgOut = ExponentialTMO(img, 1);
      %imgOut =KuangTMO(img, 'calibrated', 0.75, 'average');
      %imgOut = FerwerdaTMO(img, 100, 50, L_wa);
      %imgOut = KrawczykTMO(img);
      %imgOut = KimKautzConsistentTMO(img, 300, 0.3, 3.0, 0.5);
      %imgOut = LogarithmicTMO(img, 1, 1);
      %imgOut = NormalizeTMO(img, 1);
      %imgOut = SchlickTMO(img, 'automatic', 1, 8, 100, 0);
      %imgOut = VanHaterenTMO(img, 10);
      %imgOut = WardGlobalTMO(img, 100);
      %imgOut = MSHIST(img, 6,10,0.1);
      %%imgOut = AshikhminTMO(img, 100, 1);
      %imgOut = FerwerdaTMO(img, 100, 50, 200);
       %imgOut = LischinskiTMO(img, 50, 100);
       %%imgOut = ReinhardDevlinTMO(img, 0.5, 0.0, 1.0, 0.0, 11);
       %%imgOut = GammaTMO(img,2.2, -40, 0);
        %imgOut = TumblinTMO(img, 20, 100, 100, 100);
      
      fullFileName0=fullfile(destination, strcat(filename, format));
      imwrite(imgOut,fullFileName0);

    end
end

