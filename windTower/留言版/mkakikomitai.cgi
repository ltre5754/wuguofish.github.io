#!/usr/local/bin/perl

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++�@[ Motto Kakikomitai �h�\��ʯůd���O Ver0.864 ]  ��{����s�� 2001.02.04 / ���媩��s�� 2001.03.04 (�G��)
#+++        >>> Copyright (c) 1999.10 Tacky's Room. All rights reserved.
#+++    ��@��: Tacky �@�@�q�l�l�c >>> tackysrm@lily.freemail.ne.jp     �ӤH���� >>> http://tackysroom.com
#+++    �����: �媽�@�@�@�q�l�l�c >>> webmaster@kiddiken.net           �ӤH���� >>> http://kiddiken.net
#+++    ���ѩ�p�̤������A�ҥH�{���̫ܦh�a�賣�O�q�X��½���I�p�G������a��O�~½���A�ЧA�g�H�Φb�d���O�i�D�ڧa�I
#+++
#+++ �]�m��k
#+++
#+++ public_html (������Ƨ�)
#+++ |-- mkakikomitai           (777��711)  (����@�ӪŪ���Ƨ�)
#+++   |-- mkakikomitai.cgi     (755��700)  (�D�{��)
#+++   |-- mkakikomitai.txt     (666��600)  (�d���O���� - �}�l�ɬO�Ū�)
#+++   |-- mkakikomitai_cnt.txt (666��600)  (�ʯŪ��A�O���� - �}�l�ɬO�Ū�)
#+++   |-- mkakikomitai.cnt     (666��600)  (�p�ƾ��O���� - �}�l�ɬO�Ū�)
#+++   |-- img                  (755)       (�{�����ɸ�Ƨ�)
#+++   |   |-- *.gif                 (644)  (�{������)
#+++   |-- cicon                (755)       (�p�ƾ����ɸ�Ƨ�)
#+++   |   |-- num6_0��9.gif         (644)  (�p�ƾ�����)
#+++   |-- icon                 (755)       (�d���O���ɸ�Ƨ�)
#+++   |   |-- *.gif                 (644)  (�d���O����)
#+++   |-- old                  (755)       (�¯d�����s���m - �Ұʯd���O���e�������إ߳o�Ӹ�Ƨ�)
#+++
#+++ �@�@���A��()�����Ʀr��ܸӸ�Ƨ����ɮ׭n�]�����ɮ��v���ƭȡC
#+++ �@�@�����Fgif�ɮ׬O�ϥΤG�i��Ҧ�(Binary Mode)�W�ǥ~�A��l�ɮץ����ϥί¤�r�Ҧ�(ASCII Mode)�W�Ǩ���A���C
#+++ �@�@��mkakikomitai.lock�o���ɮצb���ݭn���ɭԷ|�۰ʲ��ͤΧR���C
#+++ �@�@���b�U���򥻳]�w��J�ɦW���ɭԡA�p�G���ݭn(�Ҧp�ɮש�b�O�B)�A�K�n�ϥΧ�����|(http://��)�ӫ��w�C
#+++
#+++ >>> ���媩��s���{...
#+++     2001.02.04(Ver0.864) >>  ����ɤ@�����u��^�v�s���[�^�h(���A�Ω󤤤媩)�C�u�@��^�Сv�M�ίd�����e�̰��r�ƪ�����C
#+++     2001.01.31(Ver0.863) >>  �ץ���R���d���O����A�d���s�����ƭȨS���M�Ū����ΡC
#+++     2001.01.22(Ver0.862) >>  �ץ�&nbsp;�y�k���~�C
#+++     2001.01.16(Ver0.861) >>  �ץ��]�w�޲z�̱M�ι��ɮɤ@�ӿ��~���ܼơC
#+++     2001.01.13(Ver0.86)  >>  �[�J�F�M���޲z�̦ӳ]���u�@��^�Сv�\��C
#+++                              �[�J�F���ѯd���O���U���\��A���ϥΪ̥i�H���u�\Ū�C�ت��O�n�`�ٹq�ܶO�C(^-^)
#+++                              �޲z�̱M�ι��ɡ��`�s�̱M�ι��ɨϥΤ��P�x�}�A�e�̨å[�J�K�X���@�w���C
#+++                              �ʯŻ����ήʯŪ��A���s����H�����s�i�J�A�C��[�j�����ܡC
#+++                              ���ܦU��GIF���ɫ��wIMG�y�k���]�w�Ҧ��A�Ϩ�i�H�[�J������׻P���ת��ȡC�o�˥i�H�קK������ܥX�Ӫ��ɭԲ��Ӳ��h�C�]���^
#+++                              �ϥ�sendmail�{���H�o�l��q�����\��[�J�F�@�ӳ]�w�ȡA�i�H���A�קK�s�ۤv�g�J���d���O���]�n�q���C
#+++     2000.10.29(Ver0.851) >>  �ץ��]�ɮ���w�{�ǿ��~�ӤޭP���p�ƾ����D�D�D�Dm(_ _)m
#+++     2000.10.28  >>  ���ɤ@����[�J�޲z�̤α`�s�̱M�ι��ɡC
#+++                     ²���ˬd���ƿ�J�d�����{�ǡC
#+++     2000.08.07  >>  �ץ��d�����e��J��檺�����~�y�k�C
#+++     2000.07.26  >>  �ץ�����h���R���d���O�������ΡC
#+++     2000.07.14  >>  �ץ����ϥίd�����D($titleset=0)���ɭԡA�u�e�X�d���v���s����O�B�����~�C
#+++     2000.07.12  >>  �ץ��ɮ���w�����D�C
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$ver                        = '0.864';                                  #(�媽�ק� - �[�J�{�������s��)
#�w�հ򥻳]�w�}�l�֢w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w
$url                        = "http://home.kimo.com.tw/j03312002";                    #���������}
$script                     = './mkakikomitai.cgi';                     #�D�{���ɦW
$logfile                    = './mkakikomitai.txt';                     #�d���O���ɦW
$lockfile                   = './mkakikomitai.lock';                    #��w���ɦW
$cntfile                    = './mkakikomitai.cnt';                     #�p�ƾ��O���ɦW (���ϥΫh�אּ'')
$logfile2                   = './mkakikomitai_cnt.txt';                 #�]�w�O���d���̯d���g�ƪ��ʯŪ��A�O���ɡC(�ϥήʯŨ�ץ��������ɮ�,���ϥΫh�אּ'')

#�n�ϥέp�ƾ����\��A�����]�w�C�ӭp�ƾ����ɪ��y�k�Csrc=���᪺�O���ɸ��|�C�p�G�A���D�C�ӹ��ɪ��j�p�A�̦n�]�[�J���(width)�M����(height)���ƭȡC
#�]�w���ɸ��|�ɡA�]�i�H������src=http://www.��/xxx.gif���y�k�ӫ��w�s�b��D�����A���H�~��L��m�����ɡC
#�p�G�����w�p�ƾ����ɡA�Чאּ''�A�K�|�ϥί¤�r�Φ���ܡC
$cnt_gif[0]                 = '<img src=./cicon/num6_0.gif width=25 height=30>';
$cnt_gif[1]                 = '<img src=./cicon/num6_1.gif width=25 height=30>';
$cnt_gif[2]                 = '<img src=./cicon/num6_2.gif width=25 height=30>';
$cnt_gif[3]                 = '<img src=./cicon/num6_3.gif width=25 height=30>';
$cnt_gif[4]                 = '<img src=./cicon/num6_4.gif width=25 height=30>';
$cnt_gif[5]                 = '<img src=./cicon/num6_5.gif width=25 height=30>';
$cnt_gif[6]                 = '<img src=./cicon/num6_6.gif width=25 height=30>';
$cnt_gif[7]                 = '<img src=./cicon/num6_7.gif width=25 height=30>';
$cnt_gif[8]                 = '<img src=./cicon/num6_8.gif width=25 height=30>';
$cnt_gif[9]                 = '<img src=./cicon/num6_9.gif width=25 height=30>';
$cnt_keta                   = 10;                                        #�p�ƾ��n��ܴX�h��Ʀr�H

$title                      = '�C�ꭷ��~�����L�C';                             #�d���O�����D
$titlelogo                  = '<img src=./img/mkakikomitai.gif width=300 height=35>';   #�d���O���D����IMG�y�k (���ϥΫh�אּ'')
$backpicture                = '<img src=http://home.kimo.com.tw/j03312002/�Ȧs/�ƪ�.gif>';                                       #�I������
$bgcolor                    = 'white';                                  #�I���C��
$tbgcolor                   = '';                                       #��g�d����檺�I���C��
$tcolor                     = 'gray';                                   #��r�C��
$linkcolor                  = 'dimgray';                                #�s���C�� (�q����X)
$vlinkcolor                 = 'dimgray';                                #�s���C�� (���g��X)
$alinkcolor                 = 'firebrick';                              #�s���C�� (���b��X)
$hovercolor                 = 'red';                                    #�s���C�� (�ƹ��g�L��)              #i000331
$pt                         = '12pt';                                   #����r�Τj�p�A��ĳ�G9,10,11,12     #i000331
$pt_mini                    = '10pt';                                    #�L�Y�r�Τj�p�A��ĳ�G8,9,10         (�媽�[�J - �M�Ω�"���ɤ@����"�s���B�C�����B�ϥΪ̮ʯŸ�T�ίd����T)
$e_font                     = "Tahoma, Verdana, Arial";                 #�^��M�ݦr�ζ�                     (�媽�[�J)
$res_gif                    = './img/res.gif';                          #�]�w���X�ȡu�^�Яd���v�����ɡC(���ϥΫh�אּ'',�K�|�H�¤�r�Φ����)
$gif_spacer                 = './img/spacer.gif';                       #�վ�Ŧ쪺DUMMY����

$name_color                 = 'white';                                  #�C�g�d�������A�d���̦W�r����T���C��
$msg_color                  = 'white';                                  #�C�g�d�������A�d�����e���I���C��

$titleset                   = 1;                                        #�C�g�d�����n�����D�ܡH(0:���n 1:�n)

$homelinklogo               = '<img src=./img/kakikomitai_linkhome.gif width=50 height=12 border=0 alt=�ӤH����>';	#�d���̭ӤH�����s������IMG�y�k (���ϥΫh�אּ'')
$maillinklogo               = '<img src=./img/kakikomitai_linkmail.gif width=50 height=12 border=0 alt=�q�l�l�c>';	#�d���̹q�l�l�c�s������IMG�y�k (���ϥΫh�אּ'')

$top_l                      = '<img src=./img/top_l_h.gif width=8 height=8>';       #�y���d���ضꨤ�ĪG������IMG�y�k (���W��) (���ϥΫh�אּ'')
$top_r                      = '<img src=./img/top_r_h.gif width=8 height=8>';       #�y���d���ضꨤ�ĪG������IMG�y�k (�k�W��) (���ϥΫh�אּ'')
$bottom_l                   = '<img src=./img/bottom_l_h.gif width=8 height=8>';    #�y���d���ضꨤ�ĪG������IMG�y�k (���U��) (���ϥΫh�אּ'')
$bottom_r                   = '<img src=./img/bottom_r_h.gif width=8 height=8>';    #�y���d���ضꨤ�ĪG������IMG�y�k (�k�U��) (���ϥΫh�אּ'')

$datamax                    = 100 ;                                     #�̷s���d�����A�O�d���d���g�� (�u�n�d���F��o�ӼƥءA�̭�����d���K�|�s�J�¯d����)
$pagemax                    = 20 ;                                      #�����i��ܤ��d���g��
$password                   = '1378246590';                                   #�޲z�̱K�X
$tag                        = 'yes';                                    #���\�ϥ�HTML�X�H(yes,no)
$resflag                    = 'yes';                                    #�̷s�^�Ъ��d���h��̳��H(yes,no)
$hostflag                   = 'yes';                                    #��ܯd���̪�HOST��}�H(yes,no)

$row                        = 4;                                        #��J�d�����e������C��(����)
$col                        = 56;                                       #��J�d�����e��������(���)
$t_width                    = 540;                                      #�C�g�d�������(�H�����p)

#�]�w�d���i�Τ��I���C��D��@�̪��]�w�G@COLORS_B = ('#666666','#003399','#990000','#669900','#cc3399','#ff6633','#cccc00');
@COLORS_B = ('deepskyblue','steelblue','dimgray','seagreen','cadetblue','darkturquoise','royalblue','darkorchid','mediumvioletred','hotpink','tomato','crimson','goldenrod','chocolate','saddlebrown',);    #(�媽�ק� - �ϥΤ�r�C��X�å[�J��h�C��)
$colb_use                   = 0;            #(0:�C��ѯd���̿�� 1:�C��Ѻ޲z�̫��w)
$colb                       = 'silver' ;    #�p�G�W�����ȬO'1'�A�����d�����ϥγo�ӫ��w���I���C��
#�]�w�d���i�Τ���r�C��D��@�̪��]�w�G@COLORS_F = ('#666666','#003399','#990000','#669900','#cc3399','#ff6633','#cccc00','#000000');
@COLORS_F = ('lightskyblue','lightsteelblue','darkgray','mediumseagreen','lightseagreen','turquoise','cornflowerblue','orchid','palevioletred','lightpink','lightsalmon','lightcoral','gold','sandybrown','peru','black');  #(�媽�ק� - �ϥΤ�r�C��X�å[�J��h�C��)
$colf_use                   = 0;            #(0:�C��ѯd���̿�� 1:�C��Ѻ޲z�̫��w)
$colf                       = 'black' ;     #�p�G�W�����ȬO'1'�A�����d�����ϥγo�ӫ��w����r�C��

#�d����檺�U����ء]�W�r�B�q�l�l�c�B�ӤH�����B���D���^�i�H�ϥΤ@�M������ܥX��
$gif_flg            = 0;                    #�Q�n�ϥίd�������ع��ɶܡH(0:���ϥ� 1:�ϥ�)

#�]�w�d����檺�U����ع���
$gif_name           = './img/kakikomitai_name.gif';     #(�W�r)
$gif_email          = './img/kakikomitai_email.gif';    #(�q�l�l�c)
$gif_home           = './img/kakikomitai_homepage.gif'; #(�ӤH����)
$gif_title          = './img/kakikomitai_title.gif';    #(���D)
$gif_message        = './img/kakikomitai_message.gif';  #(�d�����e)

$icon_use           = 'yes';                            #�d�����e�ϥι��ɶܡH(yes,no)

#���]�w�޲z�̱M�ι��ɡC���F�޲z�̥H�~�A�S����L�H�i�H�ϥγo�ӹ��ɡC
#�A�i�H�b$oiconpass���o���ݩ�A���M�ι��ɳ]�w�@�ӱK�X�A�d�����e���X�Ӫ��ɭ����ұK�X���W�r�p�G��O���Ҹ��ۦP�~�|��ܥX�ӡA�_�h�|�ϥΤ@����ɡC
#��l�N�⦳�H�n�_�R�A�Ӽg�d���A�]�������D�A���M�ι��ɱK�X�~������\�s�ΧA�������C(���ϥΫh�אּ$oiconpass = '';)
$oicon_gif    = './icon/d_ahiru.gif' ;      $oiconpass = ";           $oicon_gif_w = 32 ; $oicon_gif_h = 32 ;

#���]�w�`�s�̱M�ι��ɡC�A�i�H���A���B�ͩθg�`�W�Ӽg�d��������(�`�s��)�W�[��L���ɦp$jicon_gif[2]...[5]���A�l�������C
#�d�����e���X�Ӫ��ɭԡA�|���үd���̪��W�r�O�_��o�̩ҳ]�w��$jiconnm�@�ˡA�p�O�̫K�|�X�{�������ӤH���ɡA�����ۦ��ܤ����ɼv�T�C
$jicon_gif[0] = './icon/kuma.gif' ;         $jiconnm[0] = '�L' ;          $jicon_gif_w[0] = 38 ; $jicon_gif_h[0] = 38 ;
$jicon_gif[1] = './icon/parappa.gif' ;      $jiconnm[1] = '�L' ;          $jicon_gif_w[1] = 37 ; $jicon_gif_h[1] = 35 ;

#���]�w�d���̤@��i��ܤ����ɡC�i�H�̭ӤH�ݭn�W�[��L���ɦp$icon_gif[11]...[20]���A�l�������C
$icon_gif[0]  = './icon/ball.gif' ;         $iconnm[0]  = '�I��' ;          $icon_gif[11]  = './icon/d_ahiru.gif' ;         $iconnm[11] = ' �I��(�ժ��G��)' ;
$icon_gif[1]  = './icon/corgi.gif' ;        $iconnm[1]  = '�V�a' ;          $icon_gif_w[1]  = 32 ; $icon_gif_h[1]  = 32 ;
$icon_gif[2]  = './icon/cow.gif' ;          $iconnm[2]  = '�V��' ;          $icon_gif_w[2]  = 32 ; $icon_gif_h[2]  = 32 ;
$icon_gif[3]  = './icon/denchi.gif' ;       $iconnm[3]  = '�S��' ;          $icon_gif_w[3]  = 32 ; $icon_gif_h[3]  = 32 ;
$icon_gif[4]  = './icon/dorayaki.gif' ;     $iconnm[4]  = '�ūC' ;          $icon_gif_w[4]  = 32 ; $icon_gif_h[4]  = 32 ;
$icon_gif[5]  = './icon/duck.gif' ;         $iconnm[5]  = '�P�_' ;          $icon_gif_w[5]  = 32 ; $icon_gif_h[5]  = 32 ;
$icon_gif[6]  = './icon/h_bambi.gif' ;      $iconnm[6]  = '�ʪ�' ;          $icon_gif_w[6]  = 32 ; $icon_gif_h[6]  = 32 ;
$icon_gif[7]  = './icon/h_bear.gif' ;       $iconnm[7]  = '����' ;          $icon_gif_w[7]  = 32 ; $icon_gif_h[7]  = 32 ;
$icon_gif[8]  = './icon/h_kaeru.gif' ;      $iconnm[8]  = '��9' ;          $icon_gif_w[8]  = 32 ; $icon_gif_h[8]  = 32 ;
$icon_gif[9]  = './icon/h_momo.gif' ;       $iconnm[9]  = '��10' ;          $icon_gif_w[9]  = 32 ; $icon_gif_h[9]  = 32 ;
$icon_gif[10] = './icon/h_saru.gif' ;       $iconnm[10] = '��11' ;          $icon_gif_w[10] = 32 ; $icon_gif_h[10] = 32 ;

$icon_line          = 5 ;                   #��ܹ��ɤ@����ɡA�C����ܴX�h�ӹ��ɡH

$method             = 'POST';               #METHOD�覡(POST��GET)

#�]�w�����D������M��C�u�n�ŦX�o�M�檺���쳣�|�Q�d�I(�T��g�J�d��)�C
#  �]�w "xxx?.com" �Y�]�A�F "xxx1.com","xxx2.com" ���A�u?�v�i�H�O���󢰭Ӧr���C
#  �]�w "xxx*.com" �Y�]�A�F "xxx1.com","xxx12345.com" ���A�u*�v�i�H�O���өΥH�W������r���C
@DANGER_LIST=("xxx.com","yyy.com","zzz*.org.tw");

#�]�w�d�����e���̰��r��(�H�r���p��)�C�p�G���]�w�̰��r�ơA�אּ''�Y�i�C�o�ӼƭȤ�����]�o�Ӥj�A�̦n�O5000�ΥH�U�A�_�h�i��|�X�{���~�H���C
$maxword = '2000';		#2000�Ӧr���Y�N��1000�Ӥ���r�C

#�]�w�ʯŨ�ת��C�����O�C
@rank = ('���H','���F','���F','�������F','�g�����F','�����F','�������F','�������F','�������F','�B�����F','�������F','�Ѥ����F');
#�]�w�C�����O���ʯŸ��A�ƥج��d���g�ơC
@rankno = ('0','10','25','35','50','70','100','130','150','180','200','350');

#�A�Q�n�ھڦU�H���ʯŪ��A�ӫ��w���ɶܡH�p�G�A�ϥγo�ӼҦ��A�d���̦b�d���ɤ𶷿�ܹ��ɡC
#���~�A���ɪ��ƥض��P�ʯŨ�ת��żƤ��۹����C�]���G���޲z�̱M�ι��ɥ~�A��l�`�s�̱M�ι��ɷ|���ġ^
#��:
#  $icon_gif[0] = 'xx1.gif'; $iconnm[0] = '�Ĥ@��';
#  $icon_gif[1] = 'xx2.gif'; $iconnm[1] = '�ĤG��';
#  $icon_gif[2] = 'xx3.gif'; $iconnm[2] = '�ĤT��';
#  @rank = ('�Ĥ@��','�ĤG��','�ĤT��');
#  @rankno = ('0','10','100');  ���]�w���Ӯʯ����O�A�K�n�]�w���ӹ��ɡA�ӨC�ӹ��ɤ��O�N��o�������O�C
$icon_rank      = 0;        #0:���n�ھڮʯŪ��A���w���ɡ]�d���ɦۦ��ܹ��ɡ^ 1:�ھڮʯŪ��A���w����

#�]�wsendmail�{�������|�C������ƥi�V�����޲z�̬d�ߡC(�@��O/usr/sbin/sendmail��/usr/lib/sendmail)
#�p�G�A�Q�n�b���s�d�����ɭԧ�d����ƱH��A���q�l�l�c�A�K�n�]�w�A�_�h�i�O�d��$sendmail = "";
$sendmail       = "";

#�]�w�H�o�l��q���ɡA�n���󪺹q�l�l�c�C�u@�v���e���@�ӡu\�v�Ÿ��O�����[�W���C�p�G�S���F�u\�v�o�Ÿ��A�|�X�{Internal Server Error���~�T���C
#�]�ϥ�sendmail�{���e�H�~�ݭn�]�w�^
$smail_address  = "xxxx\@xxxx.xxxx.com.tw";

$sendsw         = 0;    #��ϥαH�o�l��q���\��ɡA�s�A�ۤv�g�J���d���O��(�H�W�����l�c�@���)�]�n�Q�ζl��q���ܡH(0:���� 1:�������n�q��)

$hiho           = 0;    #�]���u1�v�Y�i�ϥΡuhi-ho�v�Φ��ǰe�l��C�Y�Ǧ��A�����䴩�C�@���ϥ�sendmail�{���e�H�~�ݭn�]�w

#�d���K�X���[�K�{��(�ϥ�crypt��ƱN�K�X�t����)
$ango           = 1;    #0: ���ϥ� 1:�ϥΡ@�]��ĳ�ϥΡ^

#�¯d�������]�w�K���w�@�Ӹ�Ƨ�($olddir)�s��"01.txt".."10.txt"�������¯d���O���ɡC
$olddir         = './old/';     #�O�s�¯d��������Ƨ��Ҧb�C(���ϥΫh�אּ'')
$oldmax         = 100;          #�C���¯d�����i�e�Ǥ��d����C�ơC�C��W�L�o�Ӧ�C�ƫ�A�|�إߥt�@���¯d�����C

#�A�Q�n�ϥι��ynyaponika�ǲ߱b�z�d���O���u��u�j��v�\��ܡH
$nya            = 0 ;   #�d�����e������Ÿ�(<br>)�n�ξ�u(<hr>)���N�ܡH(0:�_ 1:�O)
$maru           = 1 ;   #�d���حn�ϥζꨤ�ܡH(0:�_ 1:�O)�K�p�G�u�_�v�A�h�i�H���n$top_l,r,$bottom_l,r�o�ǹ��ɡC

#=============================================================================================================================================================================================
#�]�w�Ѣ��˦���@���p�G���ϥΡA�Чאּ $css_style = "";�@���ݭn���ܡA�i�H��J����ΥH�W����r(�u�n�]�w�b���EOM�аO�����N�i�H)�C
$css_style = <<"";		#(�@���J��쪺�˦���]�w,�M�Ω��椤��textarea��input type=text,password)
style="font-size:$pt;	font-family:'�s�ө���','PMingLiU';
	color:dimgray;	background-color:white; border-width:1px; border-style:solid; border-color:lightgrey;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_style_e = <<"EOM";		#(�媽�[�J - �^�Ƥ�r��J��쪺�˦���]�w,�M�Ω��椤��[�q�l�l�c/�ӤH����/�d���s��]���)
style="font-size:$pt;	font-family:$e_font;
	color:dimgray;	background-color:white; border-width:1px; border-style:solid; border-color:lightgrey;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_button = <<"EOM";		#(�媽�[�J - ���s�M�Ϊ��˦���]�w,�M�Ω��椤��input type=submit,reset,button)
style="font-size:$pt;	font-family:'�s�ө���','PMingLiU';	line-height:12pt;
	color:gray;		background-color:white; border-width:1px; border-style:solid; border-color:lightgrey;"
	onMouseOver="this.style.color='dimgray';this.style.backgroundColor='ivory'" onMouseOut="this.style.color='gray';this.style.backgroundColor='white'"
EOM
$css_select = <<"EOM";		#(�媽�[�J - �U�Կ��M�Ϊ��˦���]�w,�M�Ω��椤��select)
style="font-size:$pt;	font-family:'�s�ө���','PMingLiU';		color:gray;		background-color:white;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_style_ = <<"EOM";		#(�媽�[�J - �w��DIE�s�������@���J��쪺�˦���]�w)
style="font-size:$pt;	font-family:'�s�ө���','PMingLiU';		color:dimgray;	background-color:white; padding-left:2px;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_style_e_ = <<"EOM";	#(�媽�[�J - �w��DIE�s�������^�Ƥ�r��J��쪺�˦���]�w)
style="font-size:$pt;	font-family:$e_font;					color:dimgray;	background-color:white; padding-left:2px;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_button_ = <<"EOM";		#(�媽�[�J - �w��DIE�s���������s�M�Ϊ��˦���]�w)
style="font-size:9pt;	font-family:'�s�ө���','PMingLiU';		color:gray;		background-color:white;"
	onMouseOver="this.style.color='dimgray';this.style.backgroundColor='ivory'" onMouseOut="this.style.color='gray';this.style.backgroundColor='white'"
EOM

#�����H�U�o�ӥ\��ت��O�n�c�@�@�d���̡A�ϥ��H���ƥئ^���d���̪��d���g�ơA�p�G���Q�ϥνг]���u$rdm = 0;�v�C
$rdm = 0;                       #�ƭȽd��O0��30�A�H���ܤơC
@DOWN = (1,2,3,5,7,10);         #�H���^���d���g�ƪ��ƥءA��ĳ�ƭȦb15�H�U�C

$kaisu_disp = 1;    #�d�����e��ܯd���̪��̷s�d���g�ơH(0:�_ 1:�O)

$ikkiflg    = 1 ;   #�A�Q�n�ϥΡu�@��^�мҦ��v�ܡH(0:�_ 1:�O)

#��d���O�ഫ��u�@��^�мҦ��v���ɭԡA�b�d����J���P�d�����e�����|�X�{�H�U��r�A�����ϥΪ̭n�`�N���Ʊ��C
$ikkimsg = <<"EOM";
<table width=500 align=center><tr><td>
���{�b�A�i�J�F�u�@��^�мҦ��v�A�A�i�H�P�ɦ^�Цh�g�d���C�u�n�b�Q�n�^�Ъ��d����C�U�����d���ءA��������d�����O��g�n�A�M��A���W����檺�u�@��^�Сv���s�Y�i�C�]�`�N�G�A�u�i�H��ܤ@�ӹ��ɡC�^�p�G�A���U�u�����@��^�Сv�A�Y�i�^�쥿�`�Ҧ��A�Ҧ��d����C�U�����d�����H�Y�����C
</td></tr></table>
EOM

#�ˬd�d�����e���M�I�y�k����
@errtag = ('table','meta','form','!--','embed','html','body','tr','td','th','a');       #�M�I�y�k����

#�w�հ򥻳]�w�����֢w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w

###############################################################################
#### Main Process  START  #####################################################
###############################################################################
$agent = $ENV{'HTTP_USER_AGENT'};
$agent =~ s/,/./g; $col2 = 1; $col2e = 1;	#(�媽�[�J - �վ�^�����bNetscape�s���������)
if ($agent =~ /Mozilla/i && $agent !~ /compatible/i && $agent !~ /Opera/i) { $col2 = 0.8; $col2e = 0.6; }	#(�媽�ק� - ���M�Ω�Opera�s����)
$ENV{'TZ'} = "CST-8";   #(�媽�ק� - �ϥΤ���Υx�W�a�Ϯɶ�)
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);    #���o�t�ήɶ�
$year  = sprintf("%02d",$year + 1900);  $month = $mon + 1;  #(�媽�ק� - ��餣�e�m���Ϊť�)
$hour  = sprintf("%02d",$hour); $min   = sprintf("%02d",$min);
$week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') [$wday];    $today = "$year/$month/$mday($week) $hour:$min";    #(�媽�ק� - �[�J�~�����)
if ($agent !~ /MSIE/i || $agent =~ /Opera/i) {	#(�媽�ק� - �DIE�s�����ϥίS�O�˦���)
	$css_style = $css_style_; $css_style_e = $css_style_e_; $css_button = $css_button_;
}
&logchk ;
&cookieget;																		#���oCOOKIE��T
&decode ;																		#�L�o�d�����e
if ( $FORM{'action'} eq 'icondisp' )	{ &icondisp ; }							#��ܹ��ɤ@����
if ( $FORM{'action'} eq 'maintenance' )	{										#�i�J�޲z�Ҧ�
	&Maintenance;
	&dataread ;																	#Ū���O����
}
if ( $FORM{'action'} eq 'update' )	{											#��s�O���ɡ]�s��ɡ^
	&update ;
	&cookieget;																	#���oCOOKIE��T
	&dataread ;																	#Ū���O����
}
if ( $FORM{'action'} eq 'regist' )	{											#�g�J�d���O��
	&regist ;
	&cookieget;																	#���oCOOKIE��T
	&dataread ;																	#Ū���O����
	&logchk ;
	$FORM{'action'} = "" ;
}
if ( $FORM{'action'} eq 'info' )		{ &info ; }								#��ܮʯŸ�满��
if ( $FORM{'action'} eq 'download' )	{ &dataread ; &download ; }				#�U���d���O��	#i001112
if ( $FORM{'action'} eq 'rankdisp' )	{ &rankdisp ; }							#��ܦU�H�ʯŪ��A
&dataread ;																		#Ū���O����
&header ;																		#���HTML����
&header2 ;
&forminput if ( $FORM{'action'} ne 'oldlogfind' || $FORM{'oldlogno'} == 0 ) ;	#��J�d�����e
&view ;																			#��ܯd���O��
&footer ;																		#���HTML����
exit;
###############################################################################
#### Main Process  END  #######################################################
###############################################################################
###<--------------------------------------------------------------
###<---   �L�o�d�����e���N�J�ܼ�
###<--------------------------------------------------------------
sub decode{
    if ($ENV{'REQUEST_METHOD'} eq "POST") {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    } else { $buffer = $ENV{'QUERY_STRING'}; }
    @pairs = split(/&/,$buffer);
    foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        if ($tag eq 'yes') {
            #�T��ϥΦM�I�y�k!!!
            foreach ( @errtag ) {
				if ($value =~ /<$_(.|\n)*/i) { &error("��p�A�d���O�T��ϥΦM�I�y�k�I"); }	#(�媽�ק� - �w��"<!--"�o�Ӱ��D�y�k�ץ���{���ʳ�)
            }
        }   else    {
            $value =~ s/</&lt;/g;
            $value =~ s/>/&gt;/g;
        }
        $value =~ s/\,/&#44;/g; #(�媽�ק� - �ϥΥb�γr��)
        $FORM{$name} = $value;
    }
    $FORM{'hp'}   =~ s/^http\:\/\///;
    $FORM{'comment'} =~ s/\r\n/<br>/g;  $FORM{'comment'} =~ s/\r|\n/<br>/g;

    for ( 1..$pagemax ) {   #i001103
        $wk = "rescomment" . $_ ;
        if ( $FORM{$wk} ne '' ) {
            $FORM{$wk} =~ s/\r\n/<br>/g;    $FORM{$wk} =~ s/\r|\n/<br>/g;
        }
    }
}
###<--------------------------------------------------------------
###<---   ��J�d�����e
###<--------------------------------------------------------------
sub forminput {
    if ( $FORM{'action'} ne 'res' ) {
        if ( $FORM{'action'} ne 'maintenance' ) {
            $c_name = $COOKIE{'nm'} ;   $c_email = $COOKIE{'em'} ;  $c_hp = $COOKIE{'hp'} ;
            $c_color = $COOKIE{'cl'} ;  $c_color_f = $COOKIE{'cl_f'} ;
            $c_icon = $COOKIE{'icon'} ; $c_pass = $COOKIE{'ps'} ;
            $c_title = '' ; $c_comment = '' ;
        }   else    {
            print "<center><font size=3 color=$tcolor>�s��d�����e</font></center><br>\n";
            if ( $FORM{'proc'} eq 'delete' )    {
                $c_name = $COOKIE{'nm'} ;   $c_email = $COOKIE{'em'} ;  $c_hp = $COOKIE{'hp'} ;
                $c_color = $COOKIE{'cl'} ;  $c_color_f = $COOKIE{'cl_f'} ;
                $c_icon = $COOKIE{'icon'} ; $c_pass = $COOKIE{'ps'} ;
                $c_title = '' ; $c_comment = '' ;
            }
        }
    }   else    {
        $c_name = $COOKIE{'nm'} ;   $c_email = $COOKIE{'em'} ;  $c_hp = $COOKIE{'hp'} ;
        $c_color = $COOKIE{'cl'} ;  $c_color_f = $COOKIE{'cl_f'} ;
        $c_icon = $COOKIE{'icon'} ; $c_pass = $COOKIE{'ps'} ;
        $c_title = '' ; $c_comment = '' ;
    }
    print "<form action=$script name=inputform method=$method>\n";
    if ( $FORM{'action'} eq 'maintenance' ) {
        print "<input type=hidden name=\"action\" value=\"update\">\n";
        print "<input type=hidden name=\"no\" value=\"$FORM{'no'}\">\n";
        print "<input type=hidden name=\"proc\" value=\"edit\">\n";
    }   else    {
        print "<input type=hidden name=\"action\" value=\"regist\">\n";                 #i001103
        print "<input type=hidden name=\"disppage\" value=$FORM{'disppage'}>\n";        #i001103
        print "<input type=hidden name=\"kflg\" value=\"$FORM{'kflg'}\">\n";            #i001103
    }
    if ( $tbgcolor ) { $padd = 2 ; } else { $padd = 1 ; }
    print "<table align=center cellspacing=0 cellpadding=$padd>\n";

    if ( $tbgcolor ) { $tbgcolor="bgcolor=$tbgcolor"; } else { $tbgcolor="";}   #u000807

    #�W�r
    print "<tr><td $tbgcolor>\n";
    if ( $gif_flg == 1 )    {
        print "<img src=\"$gif_name\"></td>\n";
    }   else    {
        print "�@�@�W�r�G</td>\n";
    }
    print "<td $tbgcolor>";
    print "<input type=text name=\"name\" size=",36 * $col2," value=\"$c_name\" $css_style></td></tr>\n";
    #�q�l�l�c
    print "<tr><td $tbgcolor>\n";   #u000807
    if ( $gif_flg == 1 )    {
        print "<img src=\"$gif_email\"></td>\n";
    }   else    {
        print "�q�l�l�c�G</td>\n";
    }
    print "<td $tbgcolor>";
	print "<input type=text name=\"email\" size=",40 * $col2e," value=\"$c_email\" $css_style_e></td></tr>\n";	#(�媽�ק� - �ϥέ^�����˦���)
    #�ӤH����
    print "<tr><td $tbgcolor>\n";
    if ( $gif_flg == 1 )    {
        print "<img src=\"$gif_home\"></td>\n";
    }   else    {
        print "�ӤH�����G</td>\n";
    }
    print "<td $tbgcolor>";
	print "<input type=text name=\"hp\" size=",40 * $col2e," value=\"http://$c_hp\" $css_style_e>\n";	#(�媽�ק� - �ϥέ^�����˦���)
    if ( $FORM{'action'} ne 'res' && $c_resno eq '' )   {
        if ( $titleset == 0 || $FORM{'kflg'} )  {                                               #i000714
            if ( $FORM{'kflg'} ) { $k = "�@��^��"; } else { $k = "�e�X�d��" }                  #(�媽�[�J - �P�O�@��^�мҦ���,�e�X���s�W����r)
            print "&nbsp;&nbsp;&nbsp;<input type=submit value=$k $css_button>&nbsp;&nbsp;\n";   #i000714
            print "&nbsp;<input type=reset value=���]��� $css_button>\n";                      #i000714
        }                                                                                       #i000714
        print "</td>\n";
    }   else    {
        print "&nbsp;&nbsp;<input type=submit value=�e�X�^�� $css_button>\n";
        print "<input type=hidden name=\"resno\" value=$FORM{'no'}>\n";
        print "&nbsp;<input type=reset value=���]��� $css_button></td>\n";
    }
    print "</tr>\n";
    #�d�����D
    if ( $FORM{'kflg'} eq '' )  {
        if  ( $FORM{'action'} ne 'res' && $c_resno eq '' )  {
            if ( $titleset == 1 ) {
                print "<tr><td $tbgcolor>\n";
                if ( $gif_flg == 1 )    {
                    print "<img src=\"$gif_title\"></td>\n";
                }   else    {
                    print "�d�����D�G</td>\n";
                }
                print "<td $tbgcolor>";
                print "<input type=text name=\"title\" size=",36 * $col2," value=\"$c_title\" $css_style>\n";
                print "&nbsp;&nbsp;&nbsp;<input type=submit value=�e�X�d�� $css_button>&nbsp;&nbsp;\n";
                print "&nbsp;<input type=reset value=���]��� $css_button></td></tr>\n";
            }
        }
        #�d�����e
        print "<tr><td $tbgcolor>\n";
        if ( $gif_flg == 1 )    {
            print "<img src=\"$gif_message\"></td>\n";
        }   else    {
            print "�d�����e�G</td>\n";
        }
        print "<td $tbgcolor>";
        if ( $nya == 0 ) { $dmy = "wrap=soft" ; } else { $dmy = "wrap=hard" ; }
		print "<textarea name=\"comment\" cols=",$col * $col2," rows=\"$row\" $dmy $css_style>$c_comment</textarea></td></tr>\n";	#(�媽�ק� - �վ����bNetscape�s���������)
        #�����C��
        if ( $colb_use != 1 && $FORM{'action'} ne 'res' && $c_resno eq '')  {
            print "<tr><td $tbgcolor>�����C��G</td>\n";
            print "<td $tbgcolor>\n";
            foreach (0 .. $#COLORS_B) {
                if ( $c_color == $_ || ($c_color eq '' && $_ == 0)) {   $dmy = "checked";   }   else    {   $dmy = "" ; }
                print "<input type=radio name=color value=\"$_\" $dmy>";
				print "<span style=font-size:$pt_mini;color:$COLORS_B[$_]>��</span>\n";	#(�媽�ק� - ��H�L�Y�r�Τj�p���)
            }
            print "</td></tr>\n";
        }
    }
    #��r�C��
    if ( $colf_use != 1 )   {
        print "<tr><td $tbgcolor>��r�C��G</td>\n";
        print "<td $tbgcolor>\n";
        foreach (0 .. $#COLORS_F) {
            if ( $c_color_f == $_ || ($c_color_f eq '' && $_ == 0)) {   $dmy = "checked";   }   else    {   $dmy = "" ; }
            print "<input type=radio name=color_f value=\"$_\" $dmy>";
			print "<span style=font-size:$pt_mini;color:$COLORS_F[$_]>��</span>\n";	#(�媽�ק� - ��H�L�Y�r�Τj�p���)
        }
        print "</td></tr>\n";
    }
    print "<tr>\n";
    #���ɿ��
    if ( $icon_rank == 0 && $icon_use eq 'yes') {
        print "<td $tbgcolor>\n";
        print "���ɿ�ܡG</td>\n";
        print "<td nowrap $tbgcolor>";
        print "<select name=\"icon\" $css_select>\n";
        $i = 0 ;
        for ( @iconnm ) {
            if ( $i == $c_icon )    {   $dmy = "selected";  }   else    {   $dmy = "" ; }
            print "<option value=$i $dmy>$iconnm[$i]\n";
            $i++ ;
        }
        print "</select>\n";
		print "&nbsp;&nbsp;<span style=font-size:$pt_mini>[ <a href=\"$script?action=icondisp\" target=_blank>���ɤ@����</a> ]</span>\n";	#(�媽�ק� - ��H�s�����覡�}��,�H�L�Y�r�Τj�p���)
        #�d���K�X
        print "&nbsp;&nbsp;&nbsp;&nbsp;�d���K�X�G\n";
        print "<input type=password name=\"pass\" size=8 value=\"$c_pass\" $css_style>&nbsp;&nbsp;(�ק�ΧR���d���ɥ�)</td>\n";
        print "</tr></table>";
        print "</form>" if ( $FORM{'kflg'} eq '' ); #i001103
        if ( $FORM{'kflg'} ne '' ) {    print "<pre>$ikkimsg</pre>" ; }
        return ;
    }
    #�d���K�X
    print "<td $tbgcolor>�d���K�X�G</td>\n";
    print "<td $tbgcolor>";
    print "<input type=password name=\"pass\" size=8 value=\"$c_pass\" $css_style>&nbsp;&nbsp;(�ק�ΧR���d���ɥ�)</td>\n";
    print "</tr></table>";
    print "</form>" if ( $FORM{'kflg'} eq '' ); #i001103
    if ( $FORM{'kflg'} ne '' ) {    print "$ikkimsg" ; }
}
###<--------------------------------------------------------------
###<---   HTML���Y����
###<--------------------------------------------------------------
sub header {
    print "Content-type: text/html; charset=big5\n\n";
    print "<html>\n<head>\n";
    print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=big5\">\n";
    if  ( $FORM{'action'} eq 'icondisp' )       {   print "<title>$title�i���ɤ@����j</title>\n";      }
    elsif   ( $FORM{'action'} eq 'rankdisp' )   {   print "<title>$title�i�U�H�ʯŪ��A�j</title>\n";    }
    elsif   ( $FORM{'action'} eq 'info' )       {   print "<title>$title�i�ʯŸ�满���j</title>\n";    }
    else {  print "<title>$title</title>\n";    }   #(�媽�ק� - �P�O��L�s�������W�٨өw�q���D)
	#<<<CSS�˦���}�l>>>
    print "<style type=\"text/css\">\n";
    print "<!--\n";
	print "a,a:link  {color:$linkcolor;text-decoration:none}\n";	#(�媽�ק� - �s����r���H����r�Τj�p)
    print "a:visited {color:$vlinkcolor;text-decoration:none}\n";
    print "a:active  {color:$alinkcolor;text-decoration:none}\n";
    print "a:hover   {color:$hovercolor;text-decoration:underline}\n";
	print "body,tr,td {font-size:$pt;word-break:break-all}\n";		#(�媽�ק� - �[�Jwork-break�ݩ�,����Q�c�N�}�a����)
    print "-->\n";
    print "</style>\n";
	#<<<CSS�˦�����>>>
    print "</head>\n";
    if ($backpicture) { $set = "background=\"$backpicture\""; if ( $bgcolor ) { $set .= " bgcolor=\"$bgcolor\"" ; } }
    elsif ($bgcolor ) { $set = "bgcolor=\"$bgcolor\""; }
    print "<body $set text=$tcolor link=$linkcolor vlink=$vlinkcolor alink=$alinkcolor>\n";
}
###<--------------------------------------------------------------
###<---   ���HTML����
###<--------------------------------------------------------------
sub header2 {
    print "<table width=100% align=center cellspacing=0 cellpadding=0><tr><td>\n";
    print "<table cellspacing=0 cellpadding=0><tr><form><td>";  #(�媽�ק� - �~�[���)
    print "<input type=button value=\"�֢ݢۢ�\" ";
    print "onClick=\"top.location.href=\'$url\'\" $css_button></td></form>\n";    #(�媽�ק� - ��H�������覡�}��)
    if ( $logfile2 && $FORM{'action'} ne 'download')    {
        print "<td width=5>&nbsp;</td><form><td><input type=button value=\"�ʯŸ�满��\" ";
        print "onClick=\"window.open('$script?action=info');\" $css_button></td></form>\n";     #(�媽�ק� - ��H�s�����覡�}��)
        print "<td width=5>&nbsp;</td><form><td><input type=button value=\"�U�H�ʯŪ��A\" ";
        print "onClick=\"window.open('$script?action=rankdisp');\" $css_button></td></form>\n"; #(�媽�ק� - ��H�s�����覡�}��)
    }
    if ( $ikkiflg == 1 )    {
        print "<td width=5>&nbsp;</td><form><td>\n";
        if ( $FORM{'kflg'} eq '' )  {
            print "<input type=button value=\"�Ұʤ@��^��\" ";
            print "onClick=\"location.href=\'$script?kflg=1\'\" $css_button></td></form>\n";  #(�媽�ק� - ��H�P�@�����覡�}��)
        }   else    {
            print "<input type=button value=\"�����@��^��\" ";
            print "onClick=\"location.href=\'$script\'\" $css_button></td></form>\n";         #(�媽�ק� - ��H�P�@�����覡�}��)
        }
    }
    if ( $#oldcnt >= 0 ) {
        print "<td width=10>&nbsp;</td><form action=\"$script\" method=\"$method\"><td nowrap>\n";  #(�媽�ק� - �[�J�ťժ����)
        print "&nbsp;&nbsp;<select name=\"oldlogno\" $css_select>\n";
        print "<option value=0>�̷s���d����";
        $i = 1 ;
        foreach ( @oldcnt ) {
            $i = sprintf("%02d",$i ) ;
            if ( $FORM{'oldlogno'} == $i ) { $dmy = "selected" ; } else { $dmy = "" ;}
            print "<option value=$i $dmy >�¯d������$i";
            $i++ ;
        }
        print "</select>\n";
        print "<input type=hidden name=\"action\" value=\"oldlogfind\">\n";
        print "<input type=submit value=\"���\" $css_button></td></form>\n";
    }
    print "</tr></table></td><td align=right>";
    if ( $cntfile ) {
        #��ܭp�ƾ�
        $edt = "%0" .$cnt_keta . "d" ;
        $COUNT = sprintf("$edt",$COUNT) ;
        if ( $cnt_gif[0] )  {
            for ( $i = 1 ; $i <= $cnt_keta ; $i++ ) {
                $c  = substr($COUNT,$i - 1 , 1 ) ;
                print "$cnt_gif[$c]";
            }
        }   else    {
            print "�s���H�� �� <font face=\"$e_font\">$COUNT</font>";   #(�媽�ק� - �ϥέ^��r����ܯ¤�r�p�ƾ�)
        }
    }   else    {
        print "&nbsp;";
    }
    print "</td></tr></table>\n";
    print "<center><br>\n";
    if ( $titlelogo )   {
        print "$titlelogo<br>\n";
    }   else    {
        print "<font size=+1 color=\"$tcolor\">$title</font><br>\n";
    }
	print "</center>\n";
}
###<--------------------------------------------------------------
###<---   ���HTML����
###<--------------------------------------------------------------
sub footer {
    #<<<���H�U���v�ŧi�������o�R���A���i���@�ק�C�]�L�����z�]���v �X �ФűN����Ƨ@�̧R���Χאּ�A�ۤv���W�r�^
	print "<div align=right><span style=font-size:9pt>\n";
    print "<a href=http://tackysroom.com target=_blank style=\"font-family:$e_font\">mkakikomitai Ver$ver Created by Tacky\'s Room</a><br>\n";
    print "����ơG<a href=http://kiddiken.net target=_blank>�ѯu���媽</a> <font face=\"$e_font\">[2001.3.4]</font></span></div>\n";
    print "</body></html>\n";
}
###<--------------------------------------------------------------
###<---   Ū���O����
###<--------------------------------------------------------------
sub dataread    {
    #Ū���O����
    if ( ( $FORM{'action'} ne 'oldlogfind' && $FORM{'action'} ne 'download' ) || $FORM{'oldlogno'} == 0 ) {
        if ( !(open(IN,"$logfile")))    {   &error("�O���� <font face=\"$e_font\">($logfile)</font> Ū�����ѡC");   }
    }   else    {
        $wk = $olddir . $FORM{'oldlogno'} . ".txt" ;
        if ( !(open(IN,"$wk")))         {   &error("�O���� <font face=\"$e_font\">($wk)</font> Ū�����ѡC");    }
    }
    @LOG = <IN>;
    close(IN);
    @RESLOG = () ; @MAINLOG = () ;
    $MAXNO = '';
    @SVLOG = () ;
    foreach ( @LOG )    {
        ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$_);
        if ( $resno eq '' ) {
            push(@MAINLOG,$_) ;
        }   else    {
            push(@RESLOG,$_) ;
        }
        push(@SVLOG,"$_");
        if ( $no >= $MAXNO ) {
            $MAXNO = $no ;
        }
    }
    if ( $FORM{'action'} ne 'oldlogfind' || $FORM{'oldlogno'} == 0 ) {  #I991220
        @RESLOG = reverse @RESLOG ;
    }                                                                   #I991220

    #<<<Ū���p�ƾ��O����
    if ( $cntfile && $FORM{'action'} ne 'download' )    {   #u001112
        if ( !(open(IN,"$cntfile")))    {   &error("�p�ƾ��O���� <font face=\"$e_font\">($cntfile)</font> Ū�����ѡC"); }
        $COUNT = <IN>;
        close(IN);
        if ( $FORM{'action'} eq '') {
            $COUNT++ ;
            if ( !(open(OUT,">$cntfile")))  {   &error("�p�ƾ��O���� <font face=\"$e_font\">($cntfile)</font> Ū�����ѡC"); }
            print OUT $COUNT;
            close(OUT);
        }
    }
}
###<--------------------------------------------------------------
###<---   ��ܯd���O��
###<--------------------------------------------------------------
sub view    {
    print "<hr width=70% size=1 noshade color=black>\n";
    #�p��d���O���һݤ�����
    $dm = @MAINLOG;
    if ( $dm % $pagemax == 0) {
        $p = $dm / $pagemax ;
    }   else    {
        $p = $dm / $pagemax + 1;
    }
    $p = sprintf("%3d",$p);
    if ( $FORM{'page'} eq "�U�@��" )    {
        if ( $FORM{'disppage'} == 0 ) { $FORM{'disppage'} = 1 } ;
        $d = ($FORM{'disppage'} + 1) * $pagemax - $pagemax ;
        $FORM{'disppage'} = $FORM{'disppage'} + 1 ;
    }   elsif   ( $FORM{'page'} eq "�W�@��" )   {
        $d = ($FORM{'disppage'} - 1) * $pagemax - $pagemax ;
        $FORM{'disppage'} = $FORM{'disppage'} - 1 ;
    }   elsif   ( $FORM{'disppage'} ne "" )     {       #I991123
        $d = $FORM{'disppage'} * $pagemax - $pagemax ;  #I991123
    }   else    {
        $d = 0  ;
        $FORM{'disppage'} = 1 ;
    }
    if ( $msg_color ) { $tbbg = "bgcolor=\"$msg_color\"" ; } else { $tbbg = "" ; }
    $z = 1 ;

    if ( $FORM{'action'} eq 'download' ) { #i001112
        $d = 0 ; $pagemax = $dm ; $maru = 0 ; $maillinklogo=""; $homelinklogo=""; $icon_use = "no";
        print "<br><center><font size=3>$title</font></center>\n";
    }

    for ( $i = $d ; ( $z <= $pagemax ) && ( $i < $dm ); $i++ )  {
        ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$host,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$MAINLOG[$i]);
        if  ( ($FORM{'action'} ne 'res' || ($FORM{'action'} eq 'res' && $FORM{'no'} eq $no)) || $FORM{'action'} eq 'download' ) {   #u001112
            if  ( $FORM{'action'} ne 'res' && $FORM{'kflg'} eq '' ) {   #i001103
                print "<form action=$script method=$method>";
                print "<input type=hidden name=\"action\" value=\"res\">";
                print "<input type=hidden name=\"no\" value=\"$no\">";
                print "<input type=hidden name=\"disppage\" value=$FORM{'disppage'}>\n";    #I991123
            }
            if ( $nya == 0 ) {
                $comment =~ s/([^=^\"]|^)(http|ftp)([\w|\!\#\&\=\-\%\@\~\;\+\:\.\?\/]+)/$1<a href=\"$2$3\" target=_blank><font face=\"$e_font\"><b>LINK HERE<\/b><\/font><\/a>/g;   #(�媽�ק� - �אּLINK HERE�^��r�ˤζ}�s����)
            }   else    {
                $comment =~ s/<br>/<br><hr size=1 noshade>/g;
            }
            if ( $colf_use != 1 )   { $color_f = $COLORS_F[$color_f] ; }    #�d���̿�ܪ���r�C��
                            else    { $color_f = $colf ; }                  #�޲z�̫��w����r�C��
            if ( $colb_use != 1 )   { $color = $COLORS_B[$color] ; }        #�d���̿�ܪ��I���C��
                            else    { $color = $colb ; }                    #�޲z�̫��w���I���C��

            print "<br>\n";
            print "<table align=center cellspacing=0 cellpadding=0 width=\"$t_width\">\n";
            if ( $maru == 1 ) { #�ϥζꨤ�d���ت����X
                print "<tr>\n";
				print "<td bgcolor=$color>$top_l</td>\n";
				print "<td bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
				print "<td bgcolor=$color align=right valign=top>$top_r</td>\n";
                print "</tr>\n";
            }   else    {
                print "<tr>\n";
				if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
					print "<td bgcolor=$color colspan=3 height=8><img src=\"$gif_spacer\" width=1 height=8></td>\n";
				} else {
					print "<td bgcolor=$color colspan=3 height=8>&nbsp;</td>\n";
				}
                print "</tr>\n";
            }
            print "<tr>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "<td bgcolor=\"$color\">\n";
                if ( $titleset == 1 ) {
                    if ( !($ttl) )  {   $ttl = "(�L�D)";    }
                    print "<font color=\"$name_color\">�� $ttl</font><br>\n";
                }
                print "<font color=\"$name_color\">$name&nbsp;&nbsp;&nbsp;";
                if ( $logfile2 ne '' )  {
                    $ranking = &rankget($ksu) ;
					print "&nbsp;&nbsp;<span style=font-size:$pt_mini>($ranking)";	#(�媽�ק� - �H�L�Y�r�Τj�p���)
                    if ( $kaisu_disp == 1 ) { print "�@���<font face=\"$e_font\">$ksu</font>�g��"; }   #(�媽�ק� - �d���g�ƥέ^��r�����)
                    print "</span>\n";
                }
				print "</font>&nbsp;&nbsp;&nbsp;";	#(�媽�ק� - �ץ���{��</font>�y�k���~)
				if ( $email ne '' ) {
					if ( $maillinklogo ) { print "<a href=mailto:$email>$maillinklogo</a>\n";
					} else { print "<font color=$name_color>[ <a href=mailto:$email><font face=\"$e_font\">MAIL</font></a> ]</font>\n"; }	#(�媽�ק� - ���Ʀr��)
				}
				if ( $hp ne '' ) {
					if ( $homelinklogo ) { print "<a href=http://$hp target=_blank>$homelinklogo</a>\n";
					} else { print "<font color=$name_color>[ <a href=http://$hp target=_blank><font face=\"$e_font\">HP</font></a> ]</font>\n"; }	#(�媽�ק� - ���Ʀr��)
				}
                if  ( $FORM{'action'} ne 'res' && $FORM{'oldlogno'} == 0  && $FORM{'kflg'} eq '' && $FORM{'action'} ne 'download' ) {   #i001103
                    if ( $res_gif ) {
						print "&nbsp;&nbsp;&nbsp;&nbsp;<input type=image name=send src=\"$res_gif\" border=0 alt=\"�^�Яd��\">\n";
                    }   else    {
                        print "&nbsp;&nbsp;&nbsp;<input type=submit value=\"�^��\" $css_button>\n";
                    }
                }
            print "</td>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "</tr><tr>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "<td bgcolor=\"$color\">\n";
                print "<hr size=1 noshade color=white>";
				print "<table cellspacing=0 cellpadding=3 width=100%>\n";	#(�媽�ק� - �R����{���h�l��<div>�y�k)
				print "<tr><td $tbbg rowspan=2>\n";	#(�媽�ק� - ���Ưd�����e�ƦC)
                #��ܹ���
                if ( $icon_use eq 'yes' )   {   &icon_set($name) ;  }   else    {   print "&nbsp;"; }
				print "</td><td $tbbg width=95% valign=top>\n";	#(�媽�ק� - �d�����e�a�W���)
                print "<font color=$color_f>$comment</font>\n"; #(�媽�ק� - �ץ���{��</div>�y�k��m���~)
				print "</td></tr><tr><td $tbbg align=right valign=bottom>";	#(�媽�ק� - �d����T�a�U���)
                $no = sprintf("%d",$no);
				print "<span style=\"font-size:$pt_mini;font-family:$e_font;color:$color_f\">";	#(�媽�ק� - ���span�y�k,�۩w�^��r�ζ�,�H�L�Y�r�Τj�p���)
                if ( $hostflag eq 'yes')    {       print "($host) ";   }
				print ".. $regdate \[$no\]</span></td></tr></table><hr size=1 noshade color=white>";	#kxxk20010130
                #��ܳX�Ȧ^�����d��
                $j = 0 ;
                foreach $buf ( @RESLOG )    {
                    ($no2,$name,$email,$hp,$ttl,$comment,$regdate,$col_f,$col_b,$resno,$host,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf); #u001103
                    if ( $no eq $resno )    {
                        if ( $colf_use != 1 )   { $col_f = $COLORS_F[$col_f] ; }    #�d���̿�ܪ���r�C��]�I���C��P��d���̬ۦP�^
                                        else    { $col_f = $colf ; }                #�޲z�̫��w����r�C��
                        print "<div align=right><table cellspacing=0 cellpadding=0 width=85%>\n";
                        print "<tr><td bgcolor=\"$color\">\n";
                            print "<table cellpadding=3 cellspacing=0 width=100%>\n";
                            print "<tr><td bgcolor=\"$color\" colspan=2 nowrap>\n";
                            print "<font color=\"$name_color\">$name&nbsp;&nbsp;&nbsp;";    #(�媽�ק� - �ץ���{��</font>�y�k���~)
                            if ( $logfile2 ne '' )  {
                                $ranking = &rankget($ksu) ;
								print "&nbsp;&nbsp;<span style=font-size:$pt_mini>($ranking)";	#(�媽�ק� - �H�L�Y�r�Τj�p���)
                                if ( $kaisu_disp == 1 ) { print "�@���<font face=\"$e_font\">$ksu</font>�g��"; }   #(�媽�ק� - �d���g�ƥέ^��r�����)
                                print "</span>\n";
                            }
                            print "</font>&nbsp;&nbsp;&nbsp;";    #(�媽�ק� - �ץ���{��</font>�y�k���~)
							if ( $email ne '' ) {
								if ( $maillinklogo ) { print "<a href=mailto:$email>$maillinklogo</a>\n";
								} else { print "<font color=$name_color>[ <a href=mailto:$email><font face=\"$e_font\">MAIL</font></a> ]</font>\n"; }	#(�媽�ק� - ���Ʀr��)
							}
							if ( $hp ne '' ) {
								if ( $homelinklogo ) { print "<a href=http://$hp target=_blank>$homelinklogo</a>\n";
								} else { print "<font color=$name_color>[ <a href=http://$hp target=_blank><font face=\"$e_font\">HP</font></a> ]</font>\n"; }	#(�媽�ק� - ���Ʀr��)
							}
							print "</td></tr>\n";
							print "<tr><td $tbbg rowspan=2>\n";	#(�媽�ק� - ���Ưd�����e�ƦC)
                            #��ܹ���
                            if ( $icon_use eq 'yes' )   {   &icon_set($name) ;  }   else    {   print "&nbsp;"; }
							print "</td><td $tbbg width=95% valign=top>\n";	#(�媽�ק� - �d�����e�a�W���)
                            if ( $nya == 0 ) {
                                $comment =~ s/([^=^\"]|^)(http|ftp)([\w|\!\#\&\=\-\%\@\~\;\+\:\.\?\/]+)/$1<a href=\"$2$3\" target=_blank><font face=\"$e_font\"><b>LINK HERE<\/b><\/font><\/a>/g;   #(�媽�ק� - �אּLINK HERE�^��r�ˤζ}�s����)
                            }   else    {
                                $comment =~ s/<br>/<br><hr size=1 noshade>/g;
                            }
                            print "<font color=$col_f>$comment</font><br>\n";
							print "</td></tr><tr><td $tbbg align=right valign=bottom>";	#(�媽�ק� - �d����T�a�U���)
                            $no2 = sprintf("%d",$no2);
							print "<span style=\"font-size:$pt_mini;font-family:$e_font;color:$col_f\">";	#(�媽�ק� - ���span�y�k,�۩w�^��r�ζ�,�H�L�Y�r�Τj�p���)
                            if ( $hostflag eq 'yes')    {
                                print "($host) ";
                            }
							print ".. $regdate \[$no2\]</span></td></tr></table>\n";	#kxxk20010130
                        print "</td></tr></table></div>\n";
                        $j++;
                    }
                }
            print "</td>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "</tr>\n";
            if ( $maru == 1 ) { #�ϥζꨤ�d���ت����X
                print "<tr>\n";
                print "<td bgcolor=\"$color\">$bottom_l</td>\n";
                print "<td bgcolor=\"$color\"><img src=\"$gif_spacer\" width=1 height=1></td>\n";
                print "<td bgcolor=\"$color\" align=\"right\" valign=\"bottom\">$bottom_r</td>\n";
                print "</tr>\n";
            }   else    {
                print "<tr>\n";
				if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
					print "<td bgcolor=$color colspan=3 height=8><img src=\"$gif_spacer\" width=1 height=8></td>\n";
				} else {
					print "<td bgcolor=$color colspan=3 height=8>&nbsp;</td>\n";
				}
                print "</tr>\n";
            }
            print "</table>";   #u001103
            if ( $FORM{'kflg'} == 1 && $FORM{'action'} ne 'download' ) {    #i001112
                print "<center><input type=hidden name=\"resno$z\" value=$no>\n";   #i001103
                print "���Ч�^�ФW�����d�����e�g�b�U���o�ӯd���ء�\n"; #i001103
                print "<br><textarea name=\"rescomment$z\" cols=\"$col\" rows=\"$row\" $dmy $css_style>$c_comment</textarea></center><br>\n";   #i001103
            }   #i001103
            print "</form>\n" if ( $FORM{'kflg'} eq '' ) ;  #i001103
        }
        $z++;
    }
    print "</form>\n" if ( $FORM{'kflg'} == 1 ) ;   #i001112

    if  ( $FORM{'action'} ne 'res' && $FORM{'action'} ne 'download')    {
        $dm = @MAINLOG;
        if ( $dm % $pagemax == 0) {
            $p = $dm / $pagemax ;
        }   else    {
            $p = $dm / $pagemax + 1;
        }
        $p = sprintf("%3d",$p);
        print "<center><form action=$script method=$method>\n";
        print "<input type=hidden name=\"disppage\" value=$FORM{'disppage'}>\n";
        print "<input type=hidden name=\"action\" value=$FORM{'action'}>\n";
        print "<input type=hidden name=\"oldlogno\" value=$FORM{'oldlogno'}>\n";
        print "<input type=hidden name=\"kflg\" value=\"$FORM{'kflg'}\">\n";            #i001103
        if ( $FORM{'disppage'} != 0 && $FORM{'disppage'} !=1)   {
            print "<input type=submit name=\"page\" value=�W�@�� $css_button>\n";
        }
        if ( $FORM{'disppage'} + 1 <= $p )  {
            print "<input type=submit name=\"page\" value=�U�@�� $css_button>\n";
        }
        print "</form></center>\n";
    }
    if ( $FORM{'action'} eq 'download' ) { return; }    #i001112

    print "<hr size=1 noshade color=black>\n" ;
    print "<center><form action=\"$script\" method=\"$method\">\n";
    print "<input type=hidden name=\"action\" value=\"download\">\n";
    print "<input type=hidden name=\"oldlogno\" value=$FORM{'oldlogno'}>\n";
    print "<input type=submit value=\"�U���ثe���d���O����\" $css_button>\n";
    print "<br>�U���ɡA�Ч��ɮת������ɦW�אּ <font face=\"$e_font\">htm / html</font>�C";
    print "</form></center>\n";
    if ( $FORM{'oldlogno'} == 0 )   {
        print "<hr width=70% size=1 noshade color=black>\n";
        print "<div align=\"right\"><form action=\"$script\" method=\"$method\">";  #(�媽�ק� - �ץ���{��<form>�y�k��m���~)
        print "<font color=\"$tcolor\">\n";
		print "�d���s���G<input type=text name=\"no\" size=4 $css_style_e>\n";	#(�媽�ק� - �ϥέ^�����˦���)
        print "�K�X�G<input type=password name=\"pass\" size=10 $css_style>\n";
        print "</font>\n";
        print "<select name=\"proc\" $css_select>\n";
        print "<option value=\"edit\">�s��\n";
        print "<option value=\"delete\">�R��\n";
        print "</select>\n";
        print "<input type=hidden name=\"action\" value=\"maintenance\">\n";
        print "<input type=hidden name=\"oldlogno\" value=$FORM{'oldlogno'}>\n";
        print "<input type=submit value=\"�޲z�d��\" $css_button>\n";
        print "</form></div>\n";
    }
}
###<--------------------------------------------------------------
###<---   �g�J�O����
###<--------------------------------------------------------------
sub regist  {
    #���o�d���̪����A���W��
    $host  = $ENV{'REMOTE_HOST'};
    $addr  = $ENV{'REMOTE_ADDR'};
    if ($host eq "" || $host eq "$addr") {
        ($p1,$p2,$p3,$p4) = split(/\./,$addr);
        $temp = pack("C4",$p1,$p2,$p3,$p4);
        $host = gethostbyaddr("$temp", 2);
        if ($host eq "") { $host = $addr; }
    }
    #�ˬd�M�I�y�k����
    foreach $buf(@DANGER_LIST){
        if ( $buf ) {
            $buf=~ s/\./\\./g;      $buf=~ s/\?/\./g;       $buf=~ s/\*/\.\*/g;
            if ($host =~ /$buf/gi) { &error("��p�A�A���ݪ�����W�٤w�Q�T��b�o�ӯd���O�ϥΡC"); }
        }
    }
    if ( $FORM{'name'} eq '')   {   &error("�d�U�A���j�W�a^^"); }
    if ( $FORM{'kflg'} eq '' ) {    #i001103
        if ( $FORM{'comment'} eq '')    {   &error("�мg�U�y�������e"); }
        if ( $maxword ne '' && (length($FORM{'comment'}) > $maxword))   {   &error("�A���d�����e�Ӫ��F�C�d�����e���i�W�L <font face=\"$e_font\">$maxword</font> �Ӧr���I"); }
    }                               #i001103
	for ( $i = $pagemax ; $i >= 1 ; $i-- )	{
		$wk = "resno" . $i ;
		$rno = $FORM{$wk} ;
		$wk = "rescomment" . $i ;
		$rcom = $FORM{$wk} ;
		if ( $rno ne '' && $rcom ne '' )	{
			if ( $maxword ne '' && (length($rcom) > $maxword))	{	&error("�A���d�����e�Ӫ��F�C�d�����e���i�W�L <font face=\"$e_font\">$maxword</font> �Ӧr���I");	}
		}
	}
    &filelock ;	#�ɮ���w
    &dataread ;	#Ū���O����

    if ( $FORM{'kflg'} eq '' ) {    #i001103
    ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$SVLOG[0]);
    if ( $name eq $FORM{'name'} && $ttl eq $FORM{'title'} && $comment eq $FORM{'comment'} ) {
        &fileunlock ;   &error("����A���g�J�@�Ҥ@�˪��d���C�i��A���ƫ��F�⦸���s�ơI") ;
    }
    if ( $logfile2 ne '' && ( $FORM{'action'} ne 'oldlogfind' || $FORM{'oldlogno'} == 0 ))  {
        if ( !(open(IN2,"$logfile2")))  {   &fileunlock ;   &error("�ʯŪ��A�O���� <font face=\"$e_font\">($logfile2)</font> Ū�����ѡC");  }
        $flg = 0 ;
        while ( <IN2> ) {
            ($n,$k) = split(/,/,$_);
            $k =~ s/\n//;
            if ( $FORM{'name'} eq $n )  {
                if ( $rdm != 0 )    {
                    #���H?�^���d���g��
                    srand(time ^ ($$ + ($$ << 15)));
                    $w  = int(rand(30)) ;
                    $p = 0 ;
                    #���ھ�$rdm���]�w�^���d���g��
                    if ( $w % $rdm == 0 )  {
                        $k  = $k - $DOWN[int(rand($#DOWN))] ;
                        if ( $k < 0 ) { $k = 0 ; }
                    }   else    {
                        $k++;
                    }
                }   else    {
                    $k++ ;
                }
                $dcnt = $k ;
                $flg = 9;
            }
            push(@sv,"$n,$k\n");
        }
        if ( $flg == 0 )    {
            push(@sv,"$FORM{'name'},1\n");
            $dcnt = 1;
        }
        close(IN2);
        if ( !(open(OUT2,">$logfile2")))    {   &fileunlock ;   &error("�ʯŪ��A�O���� <font face=\"$e_font\">($logfile2)</font> Ū�����ѡC");  }
        print OUT2 @sv;
        close(OUT2);
    }

    $dcnt2 = @SVLOG;
    if ( $dcnt2 < 1 )   {
        $no = 1;    #�Ģ��g�d��
    }   else    {
        $no = $MAXNO + 1;
    }

    #�g�J�X�Ȧ^�Ъ��d���O���ɡA�N�ӽg�d����겾�^�̳��ݪ��B�z
    if ( $resflag eq 'yes' && $FORM{'resno'} ne '') {
        $cnt = 0 ;  $oyacnt = 1 ;
        foreach $buf ( @SVLOG ) {
            ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
            if ( $oyano eq $FORM{'resno'} ) {
                $sv_title = $ttl ;
                splice(@SVLOG,$cnt,1);
                $wk = "$oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon";
                unshift(@SVLOG,$wk);
                last ;
            }
            $cnt++ ;
        }
    }   else    {
        if ( $sendmail ) {
            foreach $buf ( @SVLOG ) {
                ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                if ( $oyano eq $FORM{'resno'} ) {
                    $sv_title = $ttl ;
                    last ;
                }
            }
        }
    }

    if ( $olddir ) {    #�¯d�������B�z
        if ( !($FORM{'resno'}) && $#MAINLOG + 1 >= $datamax ) {
            ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$MAINLOG[$#MAINLOG]);
            @OLD = () ;
            if ( $#oldcnt >= 0 ) {
                if ( !(open(IN,"$oldfile")))    {   &fileunlock ;   &error("�L�h�O���� <font face=\"$e_font\">($oldfile)</font> Ū�����ѡC");   }
                @OLD = <IN>;
                close(IN);
                if ( $#OLD + 1 >= $oldmax ) {
                    $i = sprintf("%02d",$#oldcnt + 2) ;
                    $oldfile = "$olddir$i" . ".txt" ;
                    @OLD = () ;
                }
            }   else    {
                    $oldfile = "$olddir" . "01.txt" ;
            }
            $cnt = 0 ;
            @SVLOG2 = @SVLOG ; @SVLOG = () ;
            foreach $buf ( @SVLOG2 ) {
                ($oyano2,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno2,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                if ( $oyano == $oyano2 || $oyano == $resno2) {
                    unshift(@OLD,$buf) ;
                }   else    {
                    push(@SVLOG,$buf);
                }
                $cnt++ ;
            }
            if ( !(open(OUT,">$oldfile")))  {   &fileunlock ;   &error("�L�h�O���� <font face=\"$e_font\">($oldfile)</font> Ū�����ѡC");   }
            print OUT @OLD;
            close(OUT);
            #����ɮ��v��   (�媽���� - �i�]����w����0600)
            chmod(0666,"$oldfile");
        }
    }   else    {
        if ( !($FORM{'resno'}) && $#MAINLOG + 1 >= $datamax ) {
            ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$MAINLOG[$#MAINLOG]);
            @SVLOG2 = @SVLOG ; @SVLOG = () ;
            foreach $buf ( @SVLOG2 ) {
                ($oyano2,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno2,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                if ( $oyano == $oyano2 || $oyano == $resno2) {
                }   else    {
                    push(@SVLOG,$buf);
                }
            }
        }
    }
    #�d���K�X���[�K�{�ǡ]�N�K�X�t���ơ^
    if ($FORM{'pass'} ne "") { &pass_enc($FORM{'pass'}); }
    else    { $pass = '' ; }
    unshift(@SVLOG,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},$FORM{'title'},$FORM{'comment'},$today,$FORM{'color_f'},$FORM{'color'},$FORM{'resno'},$host,$dcnt,$pass,$dmy,$dmy,$FORM{'icon'}\n");
    if ( !(open(OUT,">$logfile")))  {   &fileunlock ;   &error("�O���� <font face=\"$e_font\">($logfile)</font> Ū�����ѡC");   }
    print OUT @SVLOG;
    close(OUT);
	&fileunlock ;	#�Ѱ��ɮ���w
	$wk = $smail_address ;  $wk =~ s/\\//g;
	if ( $sendmail && ($sendsw == 1 || ( $sendsw == 0 && $FORM{'email'} ne $wk ) ) ) { &SMail ; }

    }   else    {           #��i001103
    for ( $i = $pagemax ; $i >= 1 ; $i-- )  {
        $wk = "resno" . $i ;
        $rno = $FORM{$wk} ;
        $wk = "rescomment" . $i ;
        $rcom = $FORM{$wk} ;
        if ( $rno ne '' && $rcom ne '' )    {
            &dataread ;	#Ū���O����
            if ( $logfile2 ne '' )  {
                if ( !(open(IN2,"$logfile2")))  {   &fileunlock ;   &error("�ʯŪ��A�O���� <font face=\"$e_font\">($logfile2)</font> Ū�����ѡC");  }
                $flg = 0 ;
                @sv = ();
                while ( <IN2> ) {
                    ($n,$k) = split(/,/,$_);
                    $k =~ s/\n//;
                    if ( $FORM{'name'} eq $n )  {
                        $k++ ;
                        $dcnt = $k ;
                        $flg = 9;
                    }
                    push(@sv,"$n,$k\n");
                }
                if ( $flg == 0 )    {
                    push(@sv,"$FORM{'name'},1\n");
                    $dcnt = 1;
                }
                close(IN2);
                if ( !(open(OUT2,">$logfile2")))    {   &fileunlock ;   &error("�ʯŪ��A�O���� <font face=\"$e_font\">($logfile2)</font> Ū�����ѡC");  }
                print OUT2 @sv;
                close(OUT2);
            }
            $dcnt2 = @SVLOG;
            if ( $dcnt2 < 1 )   {
                $no = 1;    #�Ģ��g�d��
            }   else    {
                ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$SVLOG[0]);
                $no++;
            }
            #�g�J�X�Ȧ^�Ъ��d���O���ɡA�N�ӽg�d����겾�^�̳��ݪ��B�z
            if ( $resflag eq 'yes') {
                $cnt = 0 ;  $oyacnt = 1 ;
                foreach $buf ( @SVLOG ) {
                    ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                    if ( $oyano eq $rno )   {
                        splice(@SVLOG,$cnt,1);
                        $wk = "$oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon";
                        unshift(@SVLOG,$wk);
                        last ;
                    }
                    $cnt++ ;
                }
            }
            #�d���K�X���[�K�{�ǡ]�N�K�X�t���ơ^
            if ($FORM{'pass'} ne "") { &pass_enc($FORM{'pass'}); }
            else    { $pass = '' ; }
            unshift(@SVLOG,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},,$rcom,$today,$FORM{'color_f'},,$rno,$host,$dcnt,$pass,$dmy,$dmy,$FORM{'icon'}\n");
            if ( !(open(OUT,">$logfile")))  {   &fileunlock ;   &error("�O���� <font face=\"$e_font\">($logfile)</font> Ū�����ѡC");   }
            print OUT @SVLOG;
            close(OUT);
			&fileunlock ;	#�Ѱ��ɮ���w
			$wk = $smail_address ;  $wk =~ s/\\//g;
			if ( $sendmail && ($sendsw == 1 || ( $sendsw == 0 && $FORM{'email'} ne $wk ) ) ) { &SMail ; }	#(�媽�ק� - �ץ���{�����H�o�l��q���\�ण�䴩�@��^��)
        }
    }
    }                       #��i001103
    #COOKIE�]�w
    &cookieset ;
}
###<--------------------------------------------------------------
###<---   �޲z�Ҧ�
###<--------------------------------------------------------------
sub Maintenance {
    if ( $FORM{'pass'} eq "")   {   &error("������J�K�X�C");   }

    @DELWORD = split(/ /,$FORM{'no'});
    if ($FORM{'pass'} eq $password && $FORM{'proc'} eq 'delete' && @DELWORD > 1 ) {
        &update ;   return ;
    }

    &dataread ;	#Ū���O����
    $found = 0 ;
    foreach ( @SVLOG )  {
        ($no,$c_name,$c_email,$c_hp,$c_title,$c_comment,$regdate,$c_color_f,$c_color,$c_resno,$host,$ksu,$passwd,$dmy,$dmy,$c_icon) = split(/,/,$_);
        if ( $FORM{'no'} eq $no )   {
            if ($FORM{'pass'} ne $password && (&pass_dec($passwd))) {
                &fileunlock ;   #�Ѱ��ɮ���w
                &error("�K�X�����T�I");
            }
            $found = 1 ;
            if ( $FORM{'proc'} eq "delete" )    {
				$c_resno="";	#i010131
				&update ;
                return;
            }
            &header ;
            $c_pass = $FORM{'pass'} ;
            $c_comment =~ s/<br>/\n/g;
            &forminput ;
            last;
        }
    }
    if ( $found == 0 )  {
        &fileunlock ;   #�Ѱ��ɮ���w
        &error("�䤣��o�ӯd���s�����O���I");
    }
    &footer ;
    exit;
}

###<--------------------------------------------------------------
###<---   ��s�O����
###<--------------------------------------------------------------
sub update {
    &filelock ;	#�ɮ���w
    &dataread ;	#Ū���O����
    $j = 0 ;    @new = () ;
    foreach $buf --SVLOG) {
        ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$host,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
        if ( $FORM{'no'} eq $no || ( $FORM{'proc'} eq 'delete' && $FORM{'no'} eq $resno ) ) {           #<<<�ŦX�i�J�޲z�Ҧ�������
            if ( $FORM{'proc'} eq "edit" )  {
                #�g�J�d���K�X�Υ[�K�{�ǡ]�N�K�X�t���ơ^
                if ($FORM{'pass'} ne "") { &pass_enc($FORM{'pass'}); }
                else    { $pass = '' ; }
                if ( $rno eq '' )   {
                    push(@new,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},$FORM{'title'},$FORM{'comment'},$regdate,$FORM{'color_f'},$FORM{'color'},$resno,$host,$ksu,$pass,$dmy,$dmy,$FORM{'icon'}\n");
                }   else    {
                    push(@new,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},$ttl,$FORM{'comment'},$regdate,$FORM{'color_f'},$FORM{'color'},$resno,$host,$ksu,$pass,$dmy,$dmy,$FORM{'icon'}\n");
                }
            }
        }   else    {
            $found = 0 ;
            if ( $FORM{'proc'} eq 'delete' ) {
                @DELWORD = split(/ /,$FORM{'no'});
                foreach $word ( @DELWORD )  {
                    if ( $word && ( $no eq $word || $resno eq $word ) ) { $found = 1 ; last ; } #u000726
                }
            }
            if ( $found == 0 ) { push(@new,$buf);   }
        }
    }
    if ( !(open(OUT,">$logfile")))  {   &fileunlock ;   &error("�O���� ($logfile) Ū�����ѡC");   }
    print OUT @new;
    close(OUT);
    &fileunlock ;   #�Ѱ��ɮ���w
    $FORM{'action'} = '' ;
}
###<--------------------------------------------------------------
###<---   ��ܹ��ɤ@����
###<--------------------------------------------------------------
sub icondisp    {
    &header ;           #<<<HTML���Y����
	print "<a href=\"javascript:window.close();\">��������</a><br><center>\n";	#(�媽�ק� - �ϥ�JavaScript�s����������)
    print "������ ���ɤ@���� ������<br><br>\n";
    print "<table cellpadding=5 cellspacing=0>\n";
    $i = 0 ; $j = 0 ;
    while ( 1 ) {
        print "<tr>\n";
        for ( $ln = 1 ; $j <= $#icon_gif && $ln <= $icon_line ; ) {
            print "<td align=\"center\"><img src=\"$icon_gif[$j]\"></td>\n";
            print "<td align=\"center\">$iconnm[$j]</td>\n";
            $j++ ; $ln++ ;
        }
        if ( $j > $#icon_gif ) {
            if ( $ln < $icon_line ) {
                for ( ; $ln <= $icon_line ; ) {
                    print "<td>&nbsp;</td><td>&nbsp;</td>\n";
                    $ln++ ;
                }
            }
            print "</tr>\n";
            last ;
        }
        print "</tr>\n";
        $i++;
    }
    print "</table>";
    if ( $jiconnm[0] ne '' )    {
        print "<hr width=80% size=1>\n";
        print "<br>���`�s�̱M�ι��ɡ�<br><table cellpadding=5 cellspacing=0>\n";
        $i = 0 ; $j = 0 ;
        while ( 1 ) {
            print "<tr>\n";
            for ( $ln = 1 ; $j <= $#jicon_gif && $ln <= $icon_line ; ) {
                print "<td align=\"center\"><img src=\"$jicon_gif[$j]\"></td>\n";
                print "<td align=\"center\">$jiconnm[$j]</td>\n";
                $j++ ; $ln++ ;
            }
            if ( $j > $#jicon_gif ) {
                if ( $ln < $icon_line ) {
                    for ( ; $ln <= $icon_line ; ) {
                        print "<td>&nbsp;</td><td>&nbsp;</td>\n";
                        $ln++ ;
                    }
                }
                print "</tr>\n";
                last ;
            }
            print "</tr>\n";
            $i++;
        }
        print "</table>";
    }
    print "</center><br><br>\n";
    &footer ;           #<<<���HTML����
    exit;
}
###<--------------------------------------------------------------
###<---   ��ܥ��T������
###<--------------------------------------------------------------
sub icon_set    {
    if ( $icon_rank == 0 ) {    #���ϥήʯżҦ������p
        #�p�G�O�`�s�̯d���A�ϥα`�s�̱M�ι���
        $found = 0 ;
        for ( $k = 0 ; $k <= $#jiconnm ; $k++ ) {
            if ( $_[0] eq $jiconnm[$k] )    {
                $found = 1 ;
            if ( $jicon_gif_w[$k] != 0 ) { $dmy = "width=\"$jicon_gif_w[$k]\" height=\"$jicon_gif_h[$k]\"" ; } else { $dmy = "" ; }
                print "<img src=\"$jicon_gif[$k]\" $dmy>";
                last ;
            }
        }
        #�p�G�O�޲z�̯d���A�ϥκ޲z�̱M�ι���
        if ( $oiconpass )   {
            if ( $ango == 1 ) { $wpass = crypt($oiconpass, $oiconpass); }
            else    {   $wpass = $oiconpass ;   }
            if ( $pass eq $wpass && $found == 0 ) { #(�媽�ק� - �ץ���@�̤@�Ӥ��_��������:��`�s�̷ǽT��J�޲z�̱M�ι��ɱK�X�d�����ɭ�,�|�P�ɥX�{��رM�ι���)
                $found = 1 ;
                if ( $oicon_gif_w != 0 ) { $dmy = "width=\"$oicon_gif_w\" height=\"$oicon_gif_h\"" ; } else { $dmy = "" ; }
                print "<img src=\"$oicon_gif\" $dmy>";
            }
        }
        if ( $found == 0 )  {
            if ( !($icon) ) {   $icon = 0 ; }
            if ( $icon_gif_w[$icon] != 0 ) { $dmy = "width=\"$icon_gif_w[$icon]\" height=\"$icon_gif_h[$icon]\"" ; } else { $dmy = "" ; }
            print "<img src=\"$icon_gif[$icon]\" $dmy>";
        }
    }   else    {   #�ϥήʯżҦ������p
        #�p�G�O�޲z�̯d���A�ϥκ޲z�̱M�ι���
        $found = 0 ;
        if ( $oiconpass )   {
            if ( $ango == 1 ) { $wpass = crypt($oiconpass, $oiconpass); }
            else    {   $wpass = $oiconpass ;   }
            if ( $pass eq $wpass && $found == 0 ) { #(�媽�ק� - �ץ���@�̤@�Ӥ��_��������:��`�s�̷ǽT��J�޲z�̱M�ι��ɱK�X�d�����ɭ�,�|�P�ɥX�{��رM�ι���)
                $found = 1 ;
                if ( $oicon_gif_w != 0 ) { $dmy = "width=\"$oicon_gif_w\" height=\"$oicon_gif_h\"" ; } else { $dmy = "" ; }
                print "<img src=\"$oicon_gif\" $dmy>";
            }
        }
        if ( $found == 0 )  {
            print "<img src=\"$icon_gif[$rank_idx]\">";
        }
    }
}
###<--------------------------------------------------------------
###<---   ���oCOOKIE��T
###<--------------------------------------------------------------
sub cookieget   {
    $cookies = $ENV{'HTTP_COOKIE'};
    @pairs = split(/;/,$cookies);
    foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $name =~ s/ //g;
        $DUMMY{$name} = $value;
    }
    @pairs = split(/,/,$DUMMY{'mkakikomitai'});
    foreach $pair (@pairs) {
        ($name, $value) = split(/\!/, $pair);
        $COOKIE{$name} = $value;
    }

    if ($FORM{'name'})    { $COOKIE{'nm'}   = $FORM{'name'}; }
    if ($FORM{'email'})   { $COOKIE{'em'}   = $FORM{'email'}; }
    if ($FORM{'hp'})      { $COOKIE{'hp'}   = $FORM{'hp'}; }
    if ($FORM{'pass'})    { $COOKIE{'ps'}   = $FORM{'pass'}; }
    if ($FORM{'icon'})    { $COOKIE{'icon'} = $FORM{'icon'}; }
    if ($FORM{'color'})   { $COOKIE{'cl'}   = $FORM{'color'}; }
    if ($FORM{'color_f'}) { $COOKIE{'cl_f'} = $FORM{'color_f'}; }
}
###<--------------------------------------------------------------
###<---   �]�wCOOKIE
###<--------------------------------------------------------------
sub cookieset {
    ($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg)
        =gmtime(time + 30*24*60*60);
    $yearg  += 1900 ;
    if ($secg  < 10)  { $secg  = "0$secg";  }
    if ($ming  < 10)  { $ming  = "0$ming";  }
    if ($hourg < 10)  { $hourg = "0$hourg"; }
    if ($mdayg < 10)  { $mdayg = "0$mdayg"; }
    $mong = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
    $youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
    $date_gmt = "$youbi, $mdayg\-$mong\-$yearg $hourg:$ming:$secg GMT";
    $cook="nm\!$FORM{'name'},em\!$FORM{'email'},hp\!$FORM{'hp'},cl_f\!$FORM{'color_f'},cl\!$FORM{'color'},ps\!$FORM{'pass'},icon\!$FORM{'icon'}";
    print "Set-Cookie: mkakikomitai=$cook; expires=$date_gmt\n";
}
###<--------------------------------------------------------------
###<---   ��ܿ��~�T��
###<--------------------------------------------------------------
sub error {
    &header ;
    print "<font color=red>$_[0]</font><br><br>\n"; #(�媽�ק� - ��H���r���)
    &footer;
    exit;
}
###<--------------------------------------------------------------
###<---   �ɮ���w�{��
###<--------------------------------------------------------------
sub filelock {
    if (-e $lockfile) {
        ($ftm) = (stat($lockfile))[9];
        if ($ftm < time - 150) { unlink($lockfile); }
    }
    foreach (1 .. 5) {
        if (-e $lockfile) { sleep(1); }
        else {
            open(LOCK,">$lockfile");
            close(LOCK);
            return;
        }
    }
    &error("�P�ɦ���L�H���b�g�J�d���C�Ъ�^�W�@���ݵy��A�դ@���a�C<br>���p���p����A�i��]���d���O����w�F�A�гq���d���O�޲z�̧R����w�� <font face=\"$e_font\">($lockfile)</font> �C");
}
###<--------------------------------------------------------------
###<---   �Ѱ��ɮ���w
###<--------------------------------------------------------------
sub fileunlock {
    if (-e $lockfile) { unlink($lockfile); }
}
###<--------------------------------------------------------------
###<---   ���o�d���̪��d���g��
###<--------------------------------------------------------------
sub rankget {
    $set = 0 ;
    $tmax = $#rankno ;
    for ( $j = 0 ; $j <= $tmax ; $j++ ) {
        if ( $_[0] >= $rankno[$j] ) {
            $ranking = $rank[$j] ;
            $rank_idx = $j ;
        }
    }
    return ($ranking);
}
###<--------------------------------------------------------------
###<---   ��ܮʯŸ�满��
###<--------------------------------------------------------------
sub info    {
    &header ;           #<<<HTML���Y����
    print "<a href=\"javascript:window.close();\">��������</a><br><center>\n";  #(�媽�ק� - �אּ��������)
    print "������ �ʯŸ�满�� ������<br><br>\n";
    print "�u�n�F��H�U���d���g�ơA�A�N�i�H�ʯų�I<br><br>\n";
    $i =  0;
    print "<table cellpadding=1 cellspacing=0 bgcolor=black><tr><td>\n";
    print "<table cellpadding=5 cellspacing=1>\n";
    $k = $#rank ;
    for ( @rank )   {
        print "<tr><td bgcolor=white width=100 nowrap>$rank[$i]</td>\n";
        print "<td bgcolor=white align=right width=150 nowrap>";
        $j = $rankno[$i+1] - 1 ;
        if ( $i != $k ) {   #(�媽�ק� - �[�J�^��r��)
            print "<font face=\"$e_font\">$rankno[$i]</font> �� <font face=\"$e_font\">$j</font> �g\n";
        }   else    {
            print "<font face=\"$e_font\">$rankno[$i]</font> �g�H�W\n";
        }
        print "</td></tr>\n";
        $i++;
    }
    print "</table></td></tr></table></center><br><br>";
    &footer ;           #<<<���HTML����
    exit;
}
###<--------------------------------------------------------------
###<---   �H�o�l��q��
###<--------------------------------------------------------------
sub SMail {
    $name = $FORM{'name'};
    $email = $FORM{'email'};
    $ttl = $FORM{'title'};
    $ttl2 = $title;
	if ( $FORM{'kflg'} eq '' ) {	#(�媽�ק� - �ץ���{�����H�o�l��q���\�ण�䴩�@��^��)
		$comment = $FORM{'comment'};
	}	else	{
		$comment = "$rcom\n(�d���s��#$rno���^��)";
	}
    $comment =~ s/<br>/\n/g;

    if ($FORM{'resno'} ne "") { $ttl = "$sv_title"; }
    elsif ($FORM{'resno'} eq "" && $ttl eq "") { $ttl = "(�L�D)"; }
    $comment =~ s/&lt;/</g;
    $comment =~ s/&gt;/>/g;
    $comment =~ s/&#44;/\,/g;   #(�媽�[�J - �ഫ�b�γr��)

    if ($ttl eq "") { $ttl = "(�L�D)"; }                                    #(�媽�ק� - ��{���|�g���@��)

	#(�媽�ק� - �[�J$ttlsubj�ܼƥΨө�b�H����D�Ϥ���M��)
	if ( $FORM{'kflg'} ne '' ) {	#(�媽�[�J - �@��^�Ю���ܪ��H����D)
		$ttlsubj = "���@�g�X�ȨϥΡu�@��^�мҦ��v�g�J���d���w�g��i�d���O��";
	} else {
		if ($FORM{'resno'} eq "") {
			if ($ttl eq "(�L�D)")	{$ttlsubj = "���@�g�S�����D���s�d���w�g�g�b�d���O�W��";}
				else				{$ttlsubj = "���@�g�s���d���u$ttl�v�w�g�g�b�d���O�W��";}
		} else {
			if ($ttl eq "(�L�D)")	{$ttlsubj = "���@�g�X�Ȧ^�СB�S�����D���d���w�g�g�b�d���O�W��";}
			else					{$ttlsubj = "���@�g�X�Ȧ^�Ъ��d���u$sv_title�v�w�g�g�b�d���O�W��";}
		}
	}

    if ( !($email) ) { $email = $smail_address ; }

    if ( $hiho == 1 )   {
        open(MAIL,"| $sendmail -s \"$ttlsubj\" -f \"$email\" $smail_address") || &error("�H�H�{���X�F���D�I");  #(�媽�ק� - �H����D���$ttlsubj�ܼ�)
    }   else    {
        open(MAIL,"| $sendmail -t") || &error("�H�H�{���X�F���D�I");
        print MAIL "X-Mailer: mkakikomitai Ver$ver\n";                          #(�媽�ק� - �אּ�{���W��)
        print MAIL "To: $smail_address\n";
        if ($FORM{'email'} ne "") { print MAIL "Reply-to: $name <$email>\n"; }  #(�媽�ק� - �[�J���W�r,�L���ѹq�l�l�c�h����)
        print MAIL "Subject: $ttlsubj\n";                                       #(�媽�ק� - �H����D���$ttlsubj�ܼ�)
        print MAIL "Content-Transfer-Encoding: 8bit\n";                         #(�媽�ק� - �אּ8bit�ǰe)
        print MAIL "Content-type: text/plain; charset=big5\n";                  #(�媽�ק� - �אּ�c�餤��y�t����)
    }

    print MAIL "<<< $ttl2 >>>\n\n";
    print MAIL "�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w\n";
    print MAIL "�d���ɶ�: $today\n";
    print MAIL "�X�ȦW�r: $name\n";
    if ($FORM{'email'} ne "")   { print MAIL "�q�l�l�c: $email\n"; }            #(�媽�ק� - �L���ѹq�l�l�c�h����)
    if ($FORM{'hp'} ne "")      { print MAIL "�ӤH����: http://$FORM{'hp'}\n"; }
	if ($FORM{'kflg'} eq '')    { print MAIL "�d�����D: $ttl\n"; }				#(�媽�ק� - �@��^�Юɤ���ܼ��D)
    print MAIL "�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w\n";    #(�媽�ק� - �[�J���j��u)
    print MAIL "$comment\n";
    print MAIL "�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w�w\n";
    close(MAIL);
}
###<--------------------------------------------------------------
###<---   �K�X�[�K�{��
###<--------------------------------------------------------------
sub pass_enc {
    if ( $ango == 1 ) { $pass = crypt($_[0], $_[0]);    }
    else    {   $pass = $_[0];  }
}
###<--------------------------------------------------------------
###<---   �ˬd�K�X
###<--------------------------------------------------------------
sub pass_dec {
    if ( $ango == 1 ) {
        if ($_[0] ne '' && ( crypt($FORM{'pass'}, $_[0]) eq $_[0]) )  { return 0 ;  }
    }   else    {   if ($FORM{'pass'} eq $_[0]) {   return 0 ;  }   }
    return 1;
}
###<---------------------------------?kA?/%Դ�I? ?��?�x�Fݵf^Oj????��8#|??�o�D��2��f?�k����?��q??��$��t�J?��� ��?>T��0A�Z�_?bu?>��?u^?;lZ�j�gT8?�Z��??^�j�eRK1H?]gW���b?AJQ���lVS��3�X??���x%U�?O???$��$OGl?U?U?r-*t8��?;?�Hl9�{�YOJ?��ḿ�W��'"��?uI�|?�p?<��???v��I�cP��x��jCw�k��AI\��=,�RF-#��l1?q��;?
?0���b??�
����?��?�y2Ļ�Bc???9~]??i�c��}te��[yy?�^~��?|�ԋ�+i?T??ItlE�L?UpvF*.?�b;[��}?C���s?X?�`?�|�n��`?Y?(l)^WQ?7Pw}xF �p ID??`?\:�^??��??��B?"�׫�2~{ef�z-??1��|9&57z�w���U�خ�5$(��_�W?;[y+ (??��(��^��A�J��?f?X ?I`(*|�t�N0��F�|6���p?Y'��fq???~��}<��HEN��(?L�i�AD8k��# w���Gs;��@?ı?�n��z���b/?e8??
��?��N?�^}�|gA��?�w�?e�b^?J???-7C�f?��??(j�k^
["c�i����u�z!�L}�n�|?�&ZU?zzbj??�wG?��ȯǲ@V,�l��0R�h�V?,g|���C
} ?]?���v?&:?f?Y���� ������l��b�b%?!�G?��~�aA.(?P/#�W��ɷ??���oC?4?���k?! ��?.� Gǡg���"??	)i��q���V,G3���� ?��D. ���	?�w?`��y?p?m�/����co��DX�t?��DMe?t�_?��aaq�ܱC:�v6&$?l]U�ُ�|��r�C�ض��kB��?D��??�b۶Ap�f????_�;?��
?K�TY{��O��?��\�uM��??o0r?\?,��(i?"��m?yef??~Y?�ۇ���A�Z?��??��B�m>L?��Hy-?_T?J\?/ubo???���mn���y��??jշ�UGL.�z?��q?3�r?&t??�v�k??�p��iS? V68��b)j?�hO��*�Bd?v�M����'���R��t�G��Gn���a���e�m?��C�Mkf�nsj?	
R???qHO?RD??�w��"(�Q>y{�X��?f��V=?	
?��۷��???U�m_]?�m�~?��wT��l��S��?g??��E![?�	f<O�ŝ��ngR����޺?X?�a?�IL��?�?_xm??&?g?�Hn��y(JUA�}?�m?�Կ�?]?$�Y`0��{ns?��?8?V�T?U�B�g]I�A?X��?P&�x�N��0ڻ}?Ҽj��Ko��
��(QPi��
I��Lu�q���k?_�g
?4��?Yr���"a?�ux�gx
?Ea0c??D^??*�J:���s,j�T<�S=B�B�@��?Q#?��?��L�������.�u?�޴���?��?f-��YX�B�B)?1�m?8?��?sz�Y�f�C����D7�k&_9��??!?5ZetkKXh��?A�4?�J��?]�QG��(;?ۦ?�e�z/B̢��%?P»#bʽ�u`q��?-??��:?Ȭ��/��g��NI-%S?��w�K?M�RY���?��il=v?" ??3�d��l=L?��?�D����??2t��s({��U��½?ݥ����D?�|��V�Z�IO:GO99?��?��?H?���V�[ۢ;Y�ra?k��J"
?w��r???,??K�����Ak?0��

tFd?���33??I2w??֮-i)??N\??��=??������@pZ��>?H*?#B???����???&�fG�`?Wq6�~?>?*�z1�C?jhe?��J?W?r??	FS�΂J�SId?W�b��
U�[,?Q�� ?�RiXW??!9ϩJ?�A?׿�i���H*{{{?w[��y???b�{??&R6HH��F?e��??�}W???x??��]���G��G3c?6��o?k[��'?C�T?? y�fv?�fu֢:H?�II_?��I~fx���?�+Z?z���??��4k��?'#?SF j�@?!D(�@S
?H????$5��7?@^_
@0?%N�ļ���ڥ����<:
)?;?��@w?A��b??��?C9��?��????��Qm/?G��$h?��?z�N??�O�[t?%Q��~ZF�L�X�H_W����)��?E?��|???(h�zr�RĹ?�M�Bo�H�S�c��"�R��b'b��?��?��
"\Rk���Ԑ�?��T�U4N���{=.?!!��
!W?r��+��#C�x��V/>??
�tu�f?�x��_ﺺކ�;����?7w����`�́K44DqP��&N?t��h���A???9G9?�h��
 �F?��P	ʨ�F(P??��h�sQ`??ch???)?�t?�R
f���a�P�?ϲ?��E��GG1�tD�U��
?02�`#��O???A?Z?bt??JU1vlBV�R	+<uCj!�P?)ª??κ��?A|H��/4����L�j?v]��M?d�l��Q?��W???`?Cs�O???K��???S�Zc
���C�s�Z��Nk�B?�1�%�Tn�~8??^M�c��O�g?��3���ŧ�:G켤�nն?�i{?z#�R��!?��[t?�O?| *?���ͩn�B?���-?,.״d�eje
?��A?�[3L3^?!Q5?�@Q2?||
|?��?7?�f?Xz?��ٸ?Y ?��ce?�o�o|z0�����j|?R?��J�l??D�[xv��T�f??ګ�Φ�xP?e|��;޻�T�s?M?{��u?<Z�r+N��"��?7!��O�w$W??�B��?�o%?7)�c���?~�E
,��??]��B?��?�ۮV������*[T����?��Pg�؊Mg?2