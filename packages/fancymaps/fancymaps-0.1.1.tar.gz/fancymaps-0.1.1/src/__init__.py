#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.colors as mpl_c

vabcb_list = ['#fb8d62', '#f7875e', '#f2815a', '#ee7b57', '#e97553', '#e56f4f',
              '#e0694b', '#dc6248', '#d75c44', '#d35640', '#ce503c', '#ca4a39',
              '#c54435', '#c13e31', '#bc382d', '#b8322a', '#b32c26', '#b22b24',
              '#b63627', '#bb412a', '#bf4b2d', '#c45630', '#c96133', '#cd6b36',
              '#d27639', '#d6803b', '#db8b3e', '#df9641', '#e4a044', '#e9ab47',
              '#edb64a', '#f2c04d', '#f6cb50', '#fbd653', '#fcdb5a', '#fddd65',
              '#fddf6f', '#fde179', '#fde484', '#fde68e', '#fde898', '#feeba2',
              '#feedad', '#feefb7', '#fef1c1', '#fef4cc', '#fef6d6', '#fff8e0',
              '#fffaea', '#fffdf5', '#ffffff', '#f5fefb', '#ecfdf8', '#e2fbf4',
              '#d9faf0', '#cff9ed', '#c6f8e9', '#bcf6e6', '#b3f5e2', '#a9f4de',
              '#a0f3db', '#96f2d7', '#8df0d3', '#83efd0', '#7aeecc', '#70edc8',
              '#67ebc5', '#61e7c1', '#61ddbf', '#62d4bc', '#63cab9', '#64c0b6',
              '#65b6b3', '#66acb1', '#66a2ae', '#6798ab', '#688ea8', '#6984a5',
              '#6a7aa3', '#6b71a0', '#6b679d', '#6c5d9a', '#6d5397', '#6e4995',
              '#6f4a98', '#70509d', '#7156a3', '#715ca9', '#7262ae', '#7368b4',
              '#746fba', '#7575bf', '#767bc5', '#7681cb', '#7787d0', '#788dd6',
              '#7993dc', '#7a99e2', '#7b9fe7', '#7ca6ed', '#7cacf3']
wdiv0_list = ['#760029', '#7b032d', '#800731', '#860b35', '#8b0e39', '#90123d',
              '#951641', '#9b1945', '#a01d49', '#a5204d', '#aa2451', '#af2755',
              '#b52b59', '#ba2e5d', '#bf3261', '#c43665', '#c93969', '#ce3d6d',
              '#d34172', '#d64777', '#d94d7c', '#dc5282', '#df5887', '#e15d8c',
              '#e46391', '#e76896', '#ea6d9a', '#ec739f', '#ef78a4', '#f27da9',
              '#f482ae', '#f787b2', '#fa8db7', '#fc92bc', '#ff97c0', '#fe9ec4',
              '#fea5c8', '#fdabcc', '#fcb2d0', '#fbb8d3', '#fbbfd7', '#fac5da',
              '#f9cbde', '#f9d1e1', '#f8d7e4', '#f8dde8', '#f7e3eb', '#f6e9ee',
              '#f6eff2', '#f5f5f5', '#eaf2f6', '#dfeff7', '#d4ecf8', '#c8e9f8',
              '#bde6f9', '#b1e3fa', '#a4dffb', '#98dcfc', '#8bd9fd', '#7ed5fe',
              '#72d1fe', '#6dcdfa', '#67c9f7', '#61c5f3', '#5bc1ef', '#55bcec',
              '#4fb8e8', '#49b4e4', '#44b0e1', '#3eacdd', '#38a8d9', '#32a3d6',
              '#2c9fd2', '#269bce', '#2097cb', '#1b93c7', '#158ec3', '#0f8abf',
              '#0986bc', '#0382b8', '#007eb4', '#0079af', '#0075ab', '#0071a6',
              '#006da1', '#00699d', '#006599', '#006194', '#005d90', '#00598b',
              '#005587', '#005183', '#004d7e', '#00497a', '#004576', '#004272',
              '#003e6e', '#003a69', '#003665']
wdiv1_list = ['#0017ab', '#061cb0', '#0d20b6', '#1325bb', '#1929c0', '#1e2dc4',
              '#2431c9', '#2935ce', '#2f39d2', '#343dd7', '#3a40db', '#3f44e0',
              '#4548e4', '#4a4ce9', '#4f50ed', '#5453f2', '#5a57f6', '#5f5bfa',
              '#645fff', '#6a63ff', '#7068ff', '#766dff', '#7c72ff', '#8277ff',
              '#877bff', '#8d80ff', '#9384ff', '#9889ff', '#9e8dff', '#a392ff',
              '#a996ff', '#ae9bff', '#b49fff', '#b9a4ff', '#bfa8ff', '#c4adff',
              '#c9b2ff', '#ccb7fe', '#cfbcfd', '#d3c1fc', '#d6c6fc', '#daccfb',
              '#ddd1fa', '#e1d6f9', '#e4dbf9', '#e7e0f8', '#ebe5f7', '#eeebf6',
              '#f2f0f6', '#f5f5f5', '#f6eff2', '#f6e9ee', '#f7e3eb', '#f8dde8',
              '#f8d7e4', '#f9d1e1', '#f9cbde', '#fac5da', '#fbbfd7', '#fbb8d3',
              '#fcb2d0', '#fdabcc', '#fea5c8', '#fe9ec4', '#ff97c0', '#fc92bc',
              '#fa8db7', '#f787b2', '#f482ae', '#f27da9', '#ef78a4', '#ec739f',
              '#ea6d9a', '#e76896', '#e46391', '#e15d8c', '#df5887', '#dc5282',
              '#d94d7c', '#d64777', '#d34172', '#ce3d6d', '#c93969', '#c43665',
              '#bf3261', '#ba2e5d', '#b52b59', '#af2755', '#aa2451', '#a5204d',
              '#a01d49', '#9b1945', '#951641', '#90123d', '#8b0e39', '#860b35',
              '#800731', '#7b032d', '#760029']
wdiv2_list = ['#870000', '#8d0201', '#930303', '#990504', '#9f0606', '#a50807',
              '#ab0a09', '#b10b0a', '#b70d0c', '#bd0f0d', '#c3100f', '#ca1211',
              '#d01412', '#d61514', '#dd1715', '#e31917', '#ea1b19', '#ed2721',
              '#ef3229', '#f13b30', '#f34436', '#f44d3c', '#f65442', '#f75c47',
              '#f8634c', '#fa6951', '#fb7056', '#fc765a', '#fe7d5f', '#ff8363',
              '#ff896b', '#fe9073', '#fd977c', '#fd9d84', '#fca38c', '#fca993',
              '#fbaf9b', '#fbb4a2', '#fabaa9', '#fac0b1', '#f9c5b8', '#f9cbbf',
              '#f8d0c6', '#f8d6cd', '#f7dbd3', '#f7e0da', '#f6e5e1', '#f6ebe8',
              '#f5f0ee', '#f5f5f5', '#e9f2f6', '#ddf0f7', '#d0edf8', '#c3eaf8',
              '#b6e7f9', '#a8e4fa', '#9ae1fb', '#8cdefc', '#7ddbfd', '#6dd7fe',
              '#62d3fd', '#5dcff9', '#58cbf4', '#53c7f0', '#4ec2ec', '#49bee8',
              '#43bae3', '#3eb6df', '#39b2db', '#34add7', '#2fa9d3', '#2aa5ce',
              '#25a1ca', '#209dc6', '#1b98c2', '#1594be', '#1090ba', '#0b8cb5',
              '#0688b1', '#0183ad', '#007fa9', '#007ba4', '#0077a0', '#00739b',
              '#006f97', '#006b93', '#00678e', '#00638a', '#005f86', '#005b81',
              '#00577d', '#005379', '#004f75', '#004b71', '#00476d', '#004369',
              '#003f65', '#003c61', '#00385d']


vabcb = mpl_c.LinearSegmentedColormap.from_list( 'vabcb', vabcb_list )
vabcb_r = mpl_c.LinearSegmentedColormap.from_list( 'vabcb_r', vabcb_list[::-1] )

wdiv0 = mpl_c.LinearSegmentedColormap.from_list( 'wdiv0', wdiv0_list )
wdiv0_r = mpl_c.LinearSegmentedColormap.from_list( 'wdiv0_r', wdiv0_list[::-1] )
wdiv1 = mpl_c.LinearSegmentedColormap.from_list( 'wdiv1', wdiv1_list )
wdiv1_r = mpl_c.LinearSegmentedColormap.from_list( 'wdiv1_r', wdiv1_list[::-1] )
wdiv2 = mpl_c.LinearSegmentedColormap.from_list( 'wdiv2', wdiv2_list )
wdiv2_r = mpl_c.LinearSegmentedColormap.from_list( 'wdiv2_r', wdiv2_list[::-1] )

bdiv0_list = \
['#fcdc64', '#fcd664', '#fcd163', '#fbcc62', '#fbc662', '#fac161', '#f8bc5f',
 '#f7b75e', '#f5b25d', '#f4ad5c', '#f2a85a', '#f0a359', '#ed9e57', '#eb9a55',
 '#e89554', '#e69152', '#e38c50', '#e0884e', '#dd834d', '#d97f4b', '#d67b49',
 '#d37747', '#cf7345', '#cb6f43', '#c86b42', '#c46740', '#c0643e', '#bc603c',
 '#b85c3a', '#b35939', '#af5537', '#ab5235', '#a64f33', '#a24c32', '#9d4830',
 '#99452e', '#94422d', '#90402b', '#8b3d29', '#863a28', '#813726', '#7c3525',
 '#783223', '#733022', '#6e2d20', '#692b1f', '#64291d', '#5f271c', '#5a251b',
 '#552319', '#502118', '#4b1f17', '#461d16', '#401b14', '#3b1913', '#361812',
 '#311610', '#2d140e', '#28120c', '#23100a', '#1f0e08', '#1a0b06', '#140704',
 '#0b0302', '#000000', '#060408', '#0c080f', '#110d14', '#151019', '#18131d',
 '#1b1621', '#1e1826', '#211a2a', '#241d2e', '#271f33', '#292237', '#2c243c',
 '#2f2740', '#322944', '#352c49', '#382f4d', '#3b3252', '#3d3556', '#40385b',
 '#433a5f', '#453e64', '#484168', '#4b446d', '#4d4771', '#504a75', '#524d7a',
 '#54517e', '#575482', '#595786', '#5b5b8a', '#5d5e8f', '#606293', '#626697',
 '#64699a', '#666d9e', '#6871a2', '#6974a6', '#6b78a9', '#6d7cad', '#6f80b0',
 '#7084b4', '#7288b7', '#738cba', '#7490bd', '#7694c0', '#7799c2', '#789dc5',
 '#79a1c7', '#7aa6c9', '#7baacb', '#7baecd', '#7cb3cf', '#7db7d0', '#7dbcd1',
 '#7dc1d2', '#7dc5d3', '#7dcad3', '#7dcfd3', '#7dd4d3', '#7cd9d2', '#7bded1',
 '#7ae3cf', '#79e8cd', '#77edca']

bdiv1_list = \
['#fcdc64', '#fcd764', '#fbd163', '#fbcc63', '#fbc663', '#fbc162', '#fabb62',
 '#fab562', '#fab061', '#faaa61', '#f9a461', '#f99e60', '#f99860', '#f8925f',
 '#f88b5f', '#f5875d', '#f2825a', '#ef7e57', '#ec7955', '#e87552', '#e5704f',
 '#e26c4c', '#df684a', '#db6347', '#d85f44', '#d55a41', '#d1563e', '#ce513c',
 '#cb4c39', '#c74836', '#c44333', '#c03e30', '#bd3a2d', '#b9352a', '#b53027',
 '#b22b24', '#ac2923', '#a62821', '#a02720', '#9a251f', '#94241e', '#8e221d',
 '#88211b', '#821f1a', '#7c1e19', '#771d18', '#711b17', '#6b1a16', '#661915',
 '#601713', '#5b1612', '#551511', '#501310', '#4a120f', '#45110e', '#400f0d',
 '#3b0e0c', '#360d0b', '#300c0a', '#2b0a09', '#250908', '#1f0706', '#170505',
 '#0c0303', '#000000', '#060408', '#0c0811', '#110c18', '#160f1e', '#1a1123',
 '#1d1428', '#20162c', '#231830', '#271a35', '#2a1c39', '#2d1f3e', '#312143',
 '#342347', '#38264c', '#3b2851', '#3f2b56', '#422d5b', '#462f5f', '#493264',
 '#4d3469', '#51376e', '#543973', '#583c79', '#5c3e7e', '#604183', '#644488',
 '#67468d', '#6b4993', '#6d4c97', '#6e519b', '#6f55a0', '#6f59a4', '#705ea8',
 '#7162ac', '#7166b0', '#726ab4', '#726fb8', '#7373bc', '#7477c0', '#747bc4',
 '#757fc8', '#7684cc', '#7688d0', '#778cd4', '#7790d8', '#7894dc', '#7999e0',
 '#799de4', '#7aa1e8', '#7aa5ec', '#7baaf0', '#7bafed', '#7ab5e9', '#7abae7',
 '#7abfe4', '#79c5e1', '#79cade', '#79cfdb', '#78d4d8', '#78d9d5', '#78ded2',
 '#78e3d0', '#77e8cd', '#77edca']

bdiv2_list = \
['#7ed9e1', '#7bd6df', '#78d3dc', '#76d0da', '#73cdd7', '#70cad5', '#6ec7d2',
 '#6bc3d0', '#68c0cd', '#65bdcb', '#63bac8', '#60b7c6', '#5db4c4', '#5bb1c1',
 '#58aebf', '#55abbc', '#53a8ba', '#50a5b8', '#4da2b5', '#4b9fb3', '#489cb1',
 '#459aae', '#4497ab', '#4394a8', '#4291a5', '#418ea1', '#418b9e', '#40889b',
 '#3f8597', '#3e8294', '#3e7f91', '#3d7c8d', '#3c798a', '#3b7687', '#3b7384',
 '#3a7080', '#396d7d', '#396a7a', '#386877', '#376574', '#366271', '#365f6d',
 '#355c6a', '#345967', '#345764', '#335461', '#32515e', '#314e5b', '#314c58',
 '#304955', '#2f4652', '#2f434f', '#2e414c', '#2d3e49', '#2d3b46', '#2c3943',
 '#2b3640', '#2b333d', '#2a313a', '#292e37', '#292c34', '#282931', '#27262e',
 '#27242b', '#262128', '#2c2129', '#33222a', '#38222c', '#3e222d', '#43222e',
 '#49232f', '#4e2330', '#532331', '#582332', '#5c2433', '#612433', '#662434',
 '#6b2435', '#6f2536', '#742537', '#792538', '#7d2539', '#82253a', '#86263b',
 '#8b263c', '#90263c', '#94263d', '#99273e', '#9d273f', '#a22740', '#a52a41',
 '#a72d42', '#aa3143', '#ac3444', '#af3745', '#b13a47', '#b43d48', '#b64049',
 '#b9434a', '#bb464b', '#bd494c', '#c04c4d', '#c24f4e', '#c5524f', '#c75550',
 '#c95851', '#cc5b52', '#ce5e53', '#d06154', '#d36455', '#d56756', '#d76a57',
 '#da6c58', '#dc6f59', '#de725a', '#e1755b', '#e3785c', '#e57b5d', '#e87e5e',
 '#ea815f', '#ec8460', '#ef8761', '#f18a62', '#f38c63', '#f68f64', '#f89265',
 '#fa9566', '#fd9867', '#ff9b68']

bdiv0 = mpl_c.LinearSegmentedColormap.from_list( 'bdiv0', bdiv0_list )
bdiv0_r = mpl_c.LinearSegmentedColormap.from_list( 'bdiv0_r', bdiv0_list[::-1] )
bdiv1 = mpl_c.LinearSegmentedColormap.from_list( 'bdiv1', bdiv1_list )
bdiv1_r = mpl_c.LinearSegmentedColormap.from_list( 'bdiv1_r', bdiv1_list[::-1] )
bdiv2 = mpl_c.LinearSegmentedColormap.from_list( 'bdiv2', bdiv2_list )
bdiv2_r = mpl_c.LinearSegmentedColormap.from_list( 'bdiv2_r', bdiv2_list[::-1] )

RdBuMod_list = \
['#610524', '#650827', '#690c2a', '#6c0f2d', '#701330', '#731633', '#771a36',
 '#7a1d39', '#7e203b', '#81243e', '#842741', '#882a44', '#8b2e46', '#8e3149',
 '#92344c', '#95374e', '#983b51', '#9c3e54', '#9f4156', '#a24459', '#a5485c',
 '#a94b5e', '#ac4e61', '#af5164', '#b35467', '#b65869', '#b95b6c', '#bc5f70',
 '#bf6273', '#c26576', '#c5697a', '#c86c7d', '#cb7080', '#ce7384', '#d17787',
 '#d47a8b', '#d77e8e', '#da8191', '#dd8495', '#e08898', '#e38b9c', '#e68f9f',
 '#e992a2', '#ec96a6', '#ef99a9', '#f29dad', '#f5a0b0', '#f9a4b4', '#fca8b7',
 '#ffabbb', '#feb0bf', '#feb5c3', '#fdbbc7', '#fcc0cb', '#fcc5cf', '#fbcad3',
 '#facfd7', '#fad4db', '#f9d8de', '#f8dde2', '#f8e2e6', '#f7e7ea', '#f6ecee',
 '#f6f0f1', '#ecf3f3', '#e3f1f1', '#daefef', '#d1edec', '#c7ebea', '#bee9e8',
 '#b4e7e6', '#abe5e3', '#a0e3e1', '#96e1df', '#8cdedc', '#81dcda', '#76dad7',
 '#70d7d4', '#6cd4d1', '#67d0ce', '#63cdca', '#5ecac7', '#5ac7c4', '#56c3c1',
 '#51c0be', '#4dbdbb', '#48bab7', '#44b7b4', '#40b3b1', '#3bb0ae', '#37adab',
 '#32aaa8', '#2ea7a4', '#29a3a1', '#25a09e', '#219d9b', '#1c9a98', '#189694',
 '#139391', '#0f908e', '#0b8d8b', '#068988', '#028685', '#008381', '#00807e',
 '#007c7b', '#007978', '#007675', '#007372', '#00706e', '#006c6b', '#006968',
 '#006665', '#006362', '#00605f', '#005d5c', '#005a59', '#005756', '#005453',
 '#005150', '#004d4d', '#004b4a', '#004847', '#004545', '#004242', '#003f3f',
 '#003c3c', '#003939']
AquaIndigo_list = \
['#003a2c', '#003d2f', '#004031', '#004334', '#004637', '#00493a', '#004c3d',
 '#004f3f', '#005242', '#005545', '#005948', '#005c4b', '#005f4e', '#006251',
 '#006554', '#006857', '#006c5a', '#006f5d', '#007260', '#007563', '#007966',
 '#007c69', '#007f6c', '#00836f', '#008672', '#028975', '#068c79', '#0a907c',
 '#0e937f', '#129682', '#169a85', '#1a9d89', '#1ea08c', '#22a48f', '#26a792',
 '#2aaa95', '#2eae99', '#32b19c', '#36b49f', '#3ab8a2', '#3ebba5', '#42bea9',
 '#46c2ac', '#4ac5af', '#4ec8b2', '#52ccb5', '#56cfb9', '#5ad2bc', '#5ed6bf',
 '#63d9c2', '#68dcc6', '#74dfca', '#81e1ce', '#8ce3d2', '#98e5d6', '#a3e7da',
 '#aee9dd', '#b9ebe1', '#c3ece4', '#ceeee8', '#d8f0eb', '#e2f2ef', '#ebf3f2',
 '#f5f5f5', '#f5f0f6', '#f5ebf6', '#f5e6f7', '#f4e1f8', '#f4dcf8', '#f4d7f9',
 '#f4d1fa', '#f4ccfb', '#f4c7fb', '#f4c1fc', '#f3bcfd', '#f3b7fe', '#f3b1fe',
 '#f3abff', '#efa8fd', '#eba4fa', '#e7a1f8', '#e49ef6', '#e09af3', '#dc97f1',
 '#d993ef', '#d590ec', '#d18cea', '#cd89e8', '#ca85e6', '#c682e3', '#c27fe1',
 '#bf7bdf', '#bb78dd', '#b774da', '#b471d8', '#b06ed6', '#ac6ad4', '#a967d1',
 '#a564cf', '#a160cd', '#9e5dcb', '#9a5ac8', '#9756c5', '#9453c2', '#9050bf',
 '#8d4dbb', '#8a49b8', '#8746b5', '#8343b2', '#8040ae', '#7d3cab', '#7a39a8',
 '#7636a5', '#7333a1', '#702f9e', '#6c2c9b', '#692998', '#662694', '#632291',
 '#5f1f8e', '#5c1c8a', '#581887', '#551584', '#521180', '#4e0e7d', '#4b0b79',
 '#470776']
NavyOrangeRed_list = \
['#00228d', '#042591', '#092895', '#0d2b98', '#122e9c', '#16319f', '#1b34a3',
 '#1f36a6', '#2339aa', '#273cad', '#2c3fb1', '#3042b4', '#3445b8', '#3847bb',
 '#3c4abf', '#414dc2', '#4550c5', '#4953c9', '#4d56cc', '#5158d0', '#555bd3',
 '#5a5ed7', '#5e61da', '#6264dd', '#6666e1', '#6a6ae3', '#6e6de5', '#7270e6',
 '#7674e7', '#7a77e8', '#7e7bea', '#827eeb', '#8682ec', '#8a85ed', '#8e89ee',
 '#928cf0', '#9690f1', '#9993f2', '#9d97f3', '#a19af4', '#a59df6', '#a9a1f7',
 '#ada4f8', '#b1a8f9', '#b5abfa', '#b9affc', '#bdb2fd', '#c1b6fe', '#c5b9ff',
 '#c8bdfe', '#cbc1fe', '#cec5fd', '#d1c9fc', '#d5cdfc', '#d8d1fb', '#dbd5fa',
 '#ded9fa', '#e2ddf9', '#e5e1f8', '#e8e5f8', '#ebe9f7', '#efedf6', '#f2f1f6',
 '#f5f5f5', '#f5f1ef', '#f6ede8', '#f6e9e2', '#f6e5db', '#f7e1d5', '#f7ddce',
 '#f8d9c8', '#f8d5c1', '#f8d1ba', '#f9cdb3', '#f9c8ad', '#fac4a6', '#fac09f',
 '#fabb98', '#fbb791', '#fbb38a', '#fcae82', '#fcaa7b', '#fda573', '#fda06c',
 '#fd9b64', '#fe965c', '#fe9154', '#ff8c4b', '#fe8746', '#fd8342', '#fc7e3f',
 '#fb793b', '#f97538', '#f87034', '#f76b30', '#f5662d', '#f46129', '#f35c25',
 '#f15621', '#f0511d', '#ee4b18', '#ec4514', '#eb3e0f', '#e9380a', '#e73104',
 '#e42a00', '#e02800', '#db2600', '#d62400', '#d22200', '#cd2000', '#c81e00',
 '#c31c00', '#bf1a00', '#ba1800', '#b61600', '#b11400', '#ac1200', '#a81000',
 '#a30e00', '#9e0c00', '#9a0a00', '#950800', '#910600', '#8c0400', '#880200',
 '#840000']
cm6BuOr_list = \
['#003387', '#00368b', '#00398e', '#003c92', '#003f95', '#004299', '#00459c',
 '#0048a0', '#004ba3', '#004ea7', '#0051aa', '#0054ae', '#0057b1', '#005ab5',
 '#005db9', '#0060bc', '#0063c0', '#0066c4', '#0069c7', '#006ccb', '#006fcf',
 '#0072d2', '#0075d6', '#0078da', '#027cdd', '#077fde', '#0c83e0', '#1186e1',
 '#168ae3', '#1b8de4', '#2090e6', '#2594e7', '#2a97e8', '#2f9aea', '#349eeb',
 '#39a1ed', '#3ea4ee', '#42a8f0', '#47abf1', '#4caef2', '#51b2f4', '#55b5f5',
 '#5ab8f7', '#5fbbf8', '#64bef9', '#68c2fb', '#6dc5fc', '#72c8fe', '#76cbff',
 '#7fcefe', '#87d1fe', '#90d4fd', '#98d7fc', '#a0d9fc', '#a9dcfb', '#b1defa',
 '#b8e1fa', '#c0e4f9', '#c8e6f9', '#d0e9f8', '#d7ebf7', '#dfeef7', '#e6f0f6',
 '#eef3f6', '#f5f5f5', '#f6f2e5', '#f6eed6', '#f7ebc6', '#f7e7b5', '#f8e3a4',
 '#f8df92', '#f9db80', '#fad76e', '#fad35a', '#fbce46', '#fcca31', '#fdc51b',
 '#fdc004', '#fabc00', '#f7b900', '#f3b600', '#efb200', '#ebaf00', '#e7ac00',
 '#e4a900', '#e0a600', '#dca300', '#d89f00', '#d59c00', '#d19900', '#cd9600',
 '#c99300', '#c69000', '#c28d00', '#be8a00', '#bb8600', '#b78300', '#b48000',
 '#b07d00', '#ac7a00', '#a97700', '#a57400', '#a27100', '#9e6e00', '#9b6b00',
 '#986800', '#946500', '#916200', '#8e5f00', '#8a5c00', '#875900', '#845600',
 '#815300', '#7d5100', '#7a4e00', '#774b00', '#744800', '#714500', '#6e4200',
 '#6a3f00', '#673d00', '#643a00', '#613700', '#5e3400', '#5b3100', '#582f00',
 '#552c00', '#522900', '#4f2600']
RdBuX_list = \
['#840000', '#880200', '#8c0400', '#910600', '#950800', '#9a0a00', '#9e0b00',
 '#a30d00', '#a70f00', '#ac1100', '#b01300', '#b51500', '#b91700', '#be1900',
 '#c21b00', '#c71d00', '#cc1f00', '#d02100', '#d52300', '#da2500', '#de2800',
 '#e32a00', '#e62e02', '#e83508', '#ea3c0d', '#ec4212', '#ed4816', '#ef4e1b',
 '#f0541f', '#f25923', '#f35e27', '#f5632b', '#f6682f', '#f76d32', '#f97236',
 '#fa773a', '#fb7b3d', '#fc8040', '#fd8544', '#ff8947', '#ff8e4e', '#fe9356',
 '#fe985f', '#fd9d66', '#fda26e', '#fca676', '#fcab7d', '#fcaf84', '#fbb48b',
 '#fbb892', '#fabc99', '#fac1a0', '#fac5a7', '#f9c9ae', '#f9cdb5', '#f8d1bb',
 '#f8d5c2', '#f8d9c8', '#f7ddcf', '#f7e1d5', '#f6e5dc', '#f6e9e2', '#f6ede8',
 '#f5f1ef', '#f5f5f5', '#edf3f6', '#e5f0f6', '#dceef7', '#d4ecf8', '#cbe9f8',
 '#c3e7f9', '#bae5fa', '#b1e2fa', '#a8e0fb', '#9fddfc', '#96dafc', '#8cd8fd',
 '#82d5fe', '#79d2ff', '#71cffe', '#6dccfb', '#68c9f9', '#64c6f7', '#5fc2f4',
 '#5bbff2', '#56bcef', '#52b9ed', '#4db6ea', '#49b2e8', '#44afe6', '#40ace3',
 '#3ba9e1', '#37a5de', '#32a2dc', '#2e9fd9', '#299cd7', '#2499d5', '#2095d2',
 '#1b92d0', '#178fcd', '#128bcb', '#0e88c8', '#0985c6', '#0482c3', '#007ec1',
 '#007bbd', '#0078b9', '#0075b6', '#0072b2', '#006eaf', '#006bab', '#0068a8',
 '#0065a4', '#0062a1', '#005f9d', '#005c9a', '#005997', '#005693', '#005390',
 '#00508c', '#004d89', '#004a86', '#004782', '#00447f', '#00417c', '#003e79',
 '#003b75', '#003972', '#00366f']

RdBuMod = mpl_c.LinearSegmentedColormap.from_list( 'RdBuMod', RdBuMod_list )
RdBuMod_r = mpl_c.LinearSegmentedColormap.from_list( 'RdBuMod_r', RdBuMod_list[::-1] )
AquaIndigo = mpl_c.LinearSegmentedColormap.from_list( 'AquaIndigo', AquaIndigo_list )
AquaIndigo_r = mpl_c.LinearSegmentedColormap.from_list( 'AquaIndigo_r', AquaIndigo_list[::-1] )
NavyOrangeRed = mpl_c.LinearSegmentedColormap.from_list( 'NavyOrangeRed', NavyOrangeRed_list )
NavyOrangeRed_r = mpl_c.LinearSegmentedColormap.from_list( 'NavyOrangeRed_r', NavyOrangeRed_list[::-1] )
cm6BuOr = mpl_c.LinearSegmentedColormap.from_list( 'cm6BuOr', cm6BuOr_list )
cm6BuOr_r = mpl_c.LinearSegmentedColormap.from_list( 'cm6BuOr_r', cm6BuOr_list[::-1] )
RdBuX = mpl_c.LinearSegmentedColormap.from_list( 'RdBuX', RdBuX_list )
RdBuX_r = mpl_c.LinearSegmentedColormap.from_list( 'RdBuX_r', RdBuX_list[::-1] )

def invert_lightness( colors ):
    shape = colors.shape
    C = colors.reshape((-1,shape[-1]))
    R = np.copy(C[:,0])
    G = np.copy(C[:,1])
    B = np.copy(C[:,2])
    A = np.copy(C[:,3])
    final = [1.-0.5*(G+B), 1.-0.5*(R+B), 1.-0.5*(R+G), A]
    return np.array(final).T.reshape(shape)

def stretch_center( cmap, fac, use_hyper=False, inv_l=False, endpoint=1.0 ):
    funs = (np.arctan, np.tan)
    if use_hyper:
        funs = (np.tanh, np.arctanh)
    xm = funs[0](fac)
    ary = (funs[1]( np.linspace(-xm*endpoint, xm*endpoint, 1024) ) + fac)/(2*fac)
    colors = cmap(ary)
    if inv_l:
        colors = invert_lightness(colors)
    return mpl_c.LinearSegmentedColormap.from_list( 'CmapCustom', colors )

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import scipy.special as scs
    im = np.linspace(0,1,100)[None,:]
    plt.imshow( im, aspect='auto', cmap=wdiv2 )

    for map in [bdiv0, bdiv1, bdiv2]:
        x = np.linspace(-1,1,256)
        x, y = np.meshgrid(x,x)

        r = x**2+y**2

        z = scs.jv(3, 30*np.sqrt(r))
        fig = plt.figure( figsize=(9,9) )
        ax = fig.add_axes( [0,0,1,1] )
        ax.imshow(z, cmap=map, aspect='auto', interpolation='bicubic')
        ax.text( 0.5, 0.99, map.name, transform=ax.transAxes, ha='center', va='top', c='white' )
        ax.set_axis_off()

    # fig.savefig('image.jpg', dpi=400)
    plt.show()

