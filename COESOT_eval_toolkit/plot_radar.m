clc; clear all; close all; warning off;

addpath('./utils/')

lim = [0,70;0,70;0,70;0,70;0,70;0,70;0,70;0,70;0,70;0,70];
% labels = {'Full Occlusion','Deformation', 'Rotation', 'Fast Motion', 'Partial Occlusion', 'Illumination Vartiation','Scale Vartiation' , 'Background Object Motion', 'Motion Blur', 'Aspect Ration Change'};
labels = {'FOC','DEF', 'ROT', 'FM', 'POC ', 'LI','SV' , 'BOM', 'MB', 'ARC'};
% legendlabels = {'Ours','ToMP101','OSTrack','AiATrack', 'MixFormer22k', 'TrDimp',  'TransT50','SiamR-CNN', 'KeepTrack', 'STARK-ST101' };
legendlabels = {'Ours','OSTrack', 'AiATrack', 'MixFormer22k', 'PrDiMP50','DiMP50', 'ATOM' };

data = [47.0 71.6 70.9 63.1 67.9 64.2  66.7 61.1 56.2 61.3;        % Ours 
%        40.0 62.2 64.8 59.6 65.7 62.2 59.2 59.9 47.0 57.1;        % ToMP101
       37.7 65.2 65.8 59.5 64.8 63.5 61.0 58.3 47.4 60.0;        %OSTrack      
       38.3 65.8 63.1 58.5 63.0 61.5 56.4 58.5 48.6 54.7;        % AiATrack
       38.3 61.9 62.4 57.7 61.1 61.2 57.4 55.4 44.2 55.5;        % MixFormer22k
%        38.0 62.6 63.8 59.2 63.7 61.0 58.4 59.5 47.7 56.6;        % TrDimp
%        38.8 68.1 65.4 60.5 65.5 62.5 59.9 60.6 46.6 57.9;        % TransT50
%        39.9 65.5 64.8 59.8 64.4 63.5 58.4 61.0 45.8 57.3;        % SiamR-CNN
%        38.9 59.3 63.2 58.9 63.4 61.4 57.6 59.2 46.8 53.9;        % KeepTrack
%        34.8 60.1 62.1 56.9 61.0 60.7 55.9 55.1 44.2 54.2;        % STARK-ST101  
         36.0 49.3 61.0 55.8 61.6 58.4 57.6 52.9 44.6 52.8;        % PrDiMP50
         36.5 59.8 61.8 58.1 62.2 59.4 58.8 55.6 45.7 52.7;        % DiMP50
         32.9 53.7 57.8 53.5 58.8 57.6 54.5 53.8 41.5 50.8;        % ATOM
%          33.1 54.8 56.2 51.9 55.4 53.6 53.3 48.8 41.1 47.2;        % SiamRPN
];



Draw_radar2(data,lim,labels,legendlabels);
