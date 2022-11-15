%% 

function trackers = config_tracker()
    trackers = {    
                    struct('name', 'DiMP18',         'publish', 'xxx');               %% NO. 1
                    struct('name', 'DiMP50',           'publish', 'xxx');            %% NO. 2
                    struct('name', 'KeepTrack',           'publish', 'xxx');            %% NO. 3
                    struct('name', 'KYS',           'publish', 'xxx');            %% NO. 4
                    struct('name', 'Ours',           'publish', 'xxx');           %% NO. 5
                    struct('name', 'PrDiMP50',           'publish', 'xxx');          %% NO. 6
                    struct('name', 'STARK-S50',           'publish', 'xxx');          %% NO. 7
                    struct('name', 'STARK-ST50',           'publish', 'xxx');             %% NO. 8
                    struct('name', 'STARK-ST101',           'publish', 'xxx');          %% NO. 9
                    struct('name', 'SuperDiMP',           'publish', 'xxx');  %% NO. 10
                    struct('name', 'SuperDiMPsimple',           'publish', 'xxx');        %% NO. 11
                    struct('name', 'TOMP50',           'publish', 'xxx');             %% NO. 12
                    struct('name', 'TOMP101',           'publish', 'xxx');          %% NO. 13
                    struct('name', 'TransT50',           'publish', 'xxx');            %% NO. 14 
                    struct('name', 'AiATrack',           'publish', 'xxx');            %% NO. 15
                    struct('name', 'ATOM',           'publish', 'xxx');            %% NO. 16
                    struct('name', 'Mixformer1k',           'publish', 'xxx');            %% NO. 17
                    struct('name', 'Mixformer22k',           'publish', 'xxx');            %% NO. 18
                    struct('name', 'OStrack',           'publish', 'xxx');            %% NO. 19
                    struct('name', 'PrDiMP18',           'publish', 'xxx');            %% NO. 20
                    struct('name', 'SiamFC-EF',           'publish', 'xxx');            %% NO. 21
                    struct('name', 'SiamRPN',           'publish', 'xxx');            %% NO. 22
                    struct('name', 'TrDiMP',           'publish', 'xxx');            %% NO. 23
                    struct('name', 'TrSiam',           'publish', 'xxx');            %% NO. 24
                    struct('name', 'RTS50',           'publish', 'xxx');            %% NO. 25
                    struct('name', 'SiamR-CNN',           'publish', 'xxx');            %% NO. 26
                    struct('name', 'SiamFC-MF',           'publish', 'xxx');            %% NO. 27
                    struct('name', 'MDNet-MF',           'publish', 'xxx');            %% NO. 28
                    struct('name', 'VITAL-MF',           'publish', 'xxx');            %% NO. 29

%                       struct('name', 'rgbtimesurface',           'publish', 'xxx');            %% NO. 25
%                       struct('name', 'rgbvoxel',           'publish', 'xxx');            %% NO. 25
%                       struct('name', 'rgbevent',           'publish', 'xxx');            %% NO. 25
%                       struct('name', 'rgbeventfusion',           'publish', 'xxx');            %% NO. 25
%                       struct('name', 'rgbrecon',           'publish', 'xxx');            %% NO. 25

%                       struct('name', 'rgbonly1',           'publish', 'xxx');            %% NO. 25                    
%                       struct('name', 'rgbonly2',           'publish', 'xxx');            %% NO. 25
%                       struct('name', 'eventimg',           'publish', 'xxx');
%                       struct('name', 'rgbvoxel',           'publish', 'xxx');
%                       struct('name', 'voxelonly',           'publish', 'xxx');

%                       struct('name', '1024',           'publish', 'xxx');            %% NO. 25
%                       struct('name', '16384',           'publish', 'xxx');            %% NO. 25



                      } ; 
end

% 15 trackers selected as the baseline for BOC score 
% function trackers = config_tracker()
%     trackers = {    
%                     struct('name', 'DiMP50',           'publish', 'xxx');            %% NO. 1
%                     struct('name', 'KeepTrack',           'publish', 'xxx');            %% NO. 2
%                     struct('name', 'KYS',           'publish', 'xxx');            %% NO. 3
%                     struct('name', 'PrDiMP50',           'publish', 'xxx');          %% NO. 4
%                     struct('name', 'STARK-S50',           'publish', 'xxx');          %% NO. 5
%                     struct('name', 'SuperDiMP',           'publish', 'xxx');  %% NO. 6
%                     struct('name', 'TOMP50',           'publish', 'xxx');             %% NO. 7
%                     struct('name', 'TransT50',           'publish', 'xxx');            %% NO. 8 
%                     struct('name', 'AiATrack',           'publish', 'xxx');            %% NO. 9
%                     struct('name', 'ATOM',           'publish', 'xxx');            %% NO. 10
%                     struct('name', 'Mixformer1k',           'publish', 'xxx');            %% NO. 11
%                     struct('name', 'OStrack',           'publish', 'xxx');            %% NO. 12
%                     struct('name', 'SiamRPN',           'publish', 'xxx');            %% NO. 13
%                     struct('name', 'TrDiMP',           'publish', 'xxx');            %% NO. 14
%                     struct('name', 'TrSiam',           'publish', 'xxx');            %% NO. 15 
%                     } ; 
% end








