for j =1:2
    if j==1
        s = 'Multi';
    end 
    if j==2
        s = 'One';
    end 
    path ='/home/ziyi/Documents/TIF/ToneMap/scene';
    for i = 1:8
        myFolder = strcat('/home/ziyi/Documents/TIF/Data/scene',strcat(int2str(i),'/',s,'-Face/'));
        destination = strcat(path,strcat(int2str(i),'/',s,'-Face/AshikhminTMO/'));

        filePattern = fullfile(myFolder, '*.tif');
        jpegFiles = dir(filePattern);

        for k = 1:length(jpegFiles)
          baseFileName = jpegFiles(k).name;
          fullFileName = fullfile(myFolder, baseFileName);
          fprintf(1, 'Now reading %s\n', fullFileName);

          t = Tiff(fullFileName, 'r');
          img = read(t);                                                                                  

          [filepath,filename,forma] = fileparts(baseFileName);
          format = '.jpg';

          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/KimKautzConsistentTMO/'));
          %imgOut = KimKautzConsistentTMO(img, 300, 0.3, 3.0, 0.5);
          imgOut = KimKautzConsistentTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);
          
          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/LogarithmicTMO/'));
          %imgOut = LogarithmicTMO(img, 1, 1);
          imgOut = LogarithmicTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);
          
          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/NormalizeTMO/'));
          %imgOut = NormalizeTMO(img, 1);
          imgOut = NormalizeTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);
   
          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/VanHaterenTMO/'));
          %imgOut = VanHaterenTMO(img, 10);
          imgOut = VanHaterenTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);
          
          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/WardGlobalTMO/'));
          %imgOut = WardGlobalTMO(img, 100);
          imgOut = WardGlobalTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);
          

          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/FerwerdaTMO/'));
          %imgOut = FerwerdaTMO(img, 100, 50, 200);
          imgOut = FerwerdaTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);
          
          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/LischinskiTMO/'));
          %imgOut = LischinskiTMO(img, 50, 100);
          imgOut = LischinskiTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);
                 
          destination = strcat(path,strcat(int2str(i),'/',s,'-Face/TumblinTMO/'));
          %imgOut = TumblinTMO(img, 20, 100, 100, 100);
          imgOut = TumblinTMO(img);
          fullFileName0=fullfile(destination, strcat(filename, format));
          imwrite(imgOut,fullFileName0);      
         
             
        end
    end
end