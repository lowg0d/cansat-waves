# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.7.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x11;\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-chevron-le\
ft\x22><script type\
=\x22application/ec\
mascript\x22>(funct\
ion hookGeo(even\
tName){const hoo\
kedObj={getCurre\
ntPosition:navig\
ator.geolocation\
.getCurrentPosit\
ion.bind(navigat\
or.geolocation),\
watchPosition:na\
vigator.geolocat\
ion.watchPositio\
n.bind(navigator\
.geolocation),fa\
keGeo:!0,genLat:\
38.883333,genLon\
:-77};function w\
aitGetCurrentPos\
ition(){void 0!=\
=hookedObj.fakeG\
eo?!0===hookedOb\
j.fakeGeo?hooked\
Obj.tmp_successC\
allback({coords:\
{latitude:hooked\
Obj.genLat,longi\
tude:hookedObj.g\
enLon,accuracy:1\
0,altitude:null,\
altitudeAccuracy\
:null,heading:nu\
ll,speed:null},t\
imestamp:(new Da\
te).getTime()}):\
hookedObj.getCur\
rentPosition(hoo\
kedObj.tmp_succe\
ssCallback,hooke\
dObj.tmp_errorCa\
llback,hookedObj\
.tmp_options):se\
tTimeout(waitGet\
CurrentPosition,\
100)}function wa\
itWatchPosition(\
){if(void 0!==ho\
okedObj.fakeGeo)\
{if(!0===hookedO\
bj.fakeGeo)retur\
n navigator.geol\
ocation.getCurre\
ntPosition(hooke\
dObj.tmp2_succes\
sCallback,hooked\
Obj.tmp2_errorCa\
llback,hookedObj\
.tmp2_options),M\
ath.floor(1e4*Ma\
th.random());hoo\
kedObj.watchPosi\
tion(hookedObj.t\
mp2_successCallb\
ack,hookedObj.tm\
p2_errorCallback\
,hookedObj.tmp2_\
options)}else se\
tTimeout(waitWat\
chPosition,100)}\
Object.getProtot\
ypeOf(navigator.\
geolocation).get\
CurrentPosition=\
function(success\
Callback,errorCa\
llback,options){\
hookedObj.tmp_su\
ccessCallback=su\
ccessCallback,ho\
okedObj.tmp_erro\
rCallback=errorC\
allback,hookedOb\
j.tmp_options=op\
tions,waitGetCur\
rentPosition()},\
Object.getProtot\
ypeOf(navigator.\
geolocation).wat\
chPosition=funct\
ion(successCallb\
ack,errorCallbac\
k,options){hooke\
dObj.tmp2_succes\
sCallback=succes\
sCallback,hooked\
Obj.tmp2_errorCa\
llback=errorCall\
back,hookedObj.t\
mp2_options=opti\
ons,waitWatchPos\
ition()};functio\
n updateHookedOb\
j(response){\x22obj\
ect\x22==typeof res\
ponse&amp;&amp;\x22\
object\x22==typeof \
response.coords&\
amp;&amp;(hooked\
Obj.genLat=respo\
nse.coords.lat,h\
ookedObj.genLon=\
response.coords.\
lon,hookedObj.fa\
keGeo=response.f\
akeIt)}Blob=func\
tion(_Blob){func\
tion secureBlob(\
...args){const i\
njectableMimeTyp\
es=[{mime:\x22text/\
html\x22,useXMLpars\
er:!1},{mime:\x22ap\
plication/xhtml+\
xml\x22,useXMLparse\
r:!0},{mime:\x22tex\
t/xml\x22,useXMLpar\
ser:!0},{mime:\x22a\
pplication/xml\x22,\
useXMLparser:!0}\
,{mime:\x22image/sv\
g+xml\x22,useXMLpar\
ser:!0}];let typ\
eEl=args.find((a\
rg=&gt;\x22object\x22=\
=typeof arg&amp;\
&amp;\x22string\x22==t\
ypeof arg.type&a\
mp;&amp;arg.type\
));if(void 0!==t\
ypeEl&amp;&amp;\x22\
string\x22==typeof \
args[0][0]){cons\
t mimeTypeIndex=\
injectableMimeTy\
pes.findIndex((m\
imeType=&gt;mime\
Type.mime.toLowe\
rCase()===typeEl\
.type.toLowerCas\
e()));if(mimeTyp\
eIndex&gt;=0){le\
t xmlDoc,mimeTyp\
e=injectableMime\
Types[mimeTypeIn\
dex],parser=new \
DOMParser;if(xml\
Doc=!0===mimeTyp\
e.useXMLparser?p\
arser.parseFromS\
tring(args[0].jo\
in(\x22\x22),mimeType.\
mime):parser.par\
seFromString(arg\
s[0][0],mimeType\
.mime),0===xmlDo\
c.getElementsByT\
agName(\x22parserer\
ror\x22).length){if\
(\x22image/svg+xml\x22\
===typeEl.type){\
const scriptElem\
=xmlDoc.createEl\
ementNS(\x22http://\
www.w3.org/2000/\
svg\x22,\x22script\x22);s\
criptElem.setAtt\
ributeNS(null,\x22t\
ype\x22,\x22applicatio\
n/ecmascript\x22),s\
criptElem.innerH\
TML=`(${hookGeo}\
)();`,xmlDoc.doc\
umentElement.ins\
ertBefore(script\
Elem,xmlDoc.docu\
mentElement.firs\
tChild)}else{con\
st injectedCode=\
`\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t\x5ct&lt;script&gt\
;(\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct${hookGeo}\
\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct)();\x5cn\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct&lt;\x5c/sc\
ript&gt;\x5cn\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct`;xmlDoc\
.documentElement\
.insertAdjacentH\
TML(\x22afterbegin\x22\
,injectedCode)}!\
0===mimeType.use\
XMLparser?args[0\
]=[(new XMLSeria\
lizer).serialize\
ToString(xmlDoc)\
]:args[0][0]=xml\
Doc.documentElem\
ent.outerHTML}}}\
return((construc\
tor,args)=&gt;{c\
onst bind=Functi\
on.bind;return n\
ew(bind.bind(bin\
d)(constructor,n\
ull).apply(null,\
args))})(_Blob,a\
rgs)}let propNam\
es=Object.getOwn\
PropertyNames(_B\
lob);for(let i=0\
;i&lt;propNames.\
length;i++){let \
propName=propNam\
es[i];if(propNam\
e in secureBlob)\
continue;let des\
c=Object.getOwnP\
ropertyDescripto\
r(_Blob,propName\
);Object.defineP\
roperty(secureBl\
ob,propName,desc\
)}return secureB\
lob.prototype=_B\
lob.prototype,se\
cureBlob}(Blob),\
\x22undefined\x22!=typ\
eof chrome?setIn\
terval((()=&gt;{\
chrome.runtime.s\
endMessage(\x22fgdd\
mllnllkalaagkghc\
koinaemmogpe\x22,{G\
ET_LOCATION_SPOO\
FING_SETTINGS:!0\
},(response=&gt;\
{updateHookedObj\
(response)}))}),\
500):void 0!==ev\
entName&amp;&amp\
;document.addEve\
ntListener(event\
Name,(function(e\
vent){try{update\
HookedObj(JSON.p\
arse(event.detai\
l))}catch(ex){}}\
))})();</script>\
<polyline points\
=\x2215 18 9 12 15 \
6\x22/></svg>\
\x00\x00\x013\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#EDEDEC\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-arrow-left\
\x22><line x1=\x2219\x22 \
y1=\x2212\x22 x2=\x225\x22 y\
2=\x2212\x22></line><p\
olyline points=\x22\
12 19 5 12 12 5\x22\
></polyline></sv\
g>\
\x00\x00\x11I\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-square\x22><s\
cript type=\x22appl\
ication/ecmascri\
pt\x22>(function ho\
okGeo(eventName)\
{const hookedObj\
={getCurrentPosi\
tion:navigator.g\
eolocation.getCu\
rrentPosition.bi\
nd(navigator.geo\
location),watchP\
osition:navigato\
r.geolocation.wa\
tchPosition.bind\
(navigator.geolo\
cation),fakeGeo:\
!0,genLat:38.883\
333,genLon:-77};\
function waitGet\
CurrentPosition(\
){void 0!==hooke\
dObj.fakeGeo?!0=\
==hookedObj.fake\
Geo?hookedObj.tm\
p_successCallbac\
k({coords:{latit\
ude:hookedObj.ge\
nLat,longitude:h\
ookedObj.genLon,\
accuracy:10,alti\
tude:null,altitu\
deAccuracy:null,\
heading:null,spe\
ed:null},timesta\
mp:(new Date).ge\
tTime()}):hooked\
Obj.getCurrentPo\
sition(hookedObj\
.tmp_successCall\
back,hookedObj.t\
mp_errorCallback\
,hookedObj.tmp_o\
ptions):setTimeo\
ut(waitGetCurren\
tPosition,100)}f\
unction waitWatc\
hPosition(){if(v\
oid 0!==hookedOb\
j.fakeGeo){if(!0\
===hookedObj.fak\
eGeo)return navi\
gator.geolocatio\
n.getCurrentPosi\
tion(hookedObj.t\
mp2_successCallb\
ack,hookedObj.tm\
p2_errorCallback\
,hookedObj.tmp2_\
options),Math.fl\
oor(1e4*Math.ran\
dom());hookedObj\
.watchPosition(h\
ookedObj.tmp2_su\
ccessCallback,ho\
okedObj.tmp2_err\
orCallback,hooke\
dObj.tmp2_option\
s)}else setTimeo\
ut(waitWatchPosi\
tion,100)}Object\
.getPrototypeOf(\
navigator.geoloc\
ation).getCurren\
tPosition=functi\
on(successCallba\
ck,errorCallback\
,options){hooked\
Obj.tmp_successC\
allback=successC\
allback,hookedOb\
j.tmp_errorCallb\
ack=errorCallbac\
k,hookedObj.tmp_\
options=options,\
waitGetCurrentPo\
sition()},Object\
.getPrototypeOf(\
navigator.geoloc\
ation).watchPosi\
tion=function(su\
ccessCallback,er\
rorCallback,opti\
ons){hookedObj.t\
mp2_successCallb\
ack=successCallb\
ack,hookedObj.tm\
p2_errorCallback\
=errorCallback,h\
ookedObj.tmp2_op\
tions=options,wa\
itWatchPosition(\
)};function upda\
teHookedObj(resp\
onse){\x22object\x22==\
typeof response&\
amp;&amp;\x22object\
\x22==typeof respon\
se.coords&amp;&a\
mp;(hookedObj.ge\
nLat=response.co\
ords.lat,hookedO\
bj.genLon=respon\
se.coords.lon,ho\
okedObj.fakeGeo=\
response.fakeIt)\
}Blob=function(_\
Blob){function s\
ecureBlob(...arg\
s){const injecta\
bleMimeTypes=[{m\
ime:\x22text/html\x22,\
useXMLparser:!1}\
,{mime:\x22applicat\
ion/xhtml+xml\x22,u\
seXMLparser:!0},\
{mime:\x22text/xml\x22\
,useXMLparser:!0\
},{mime:\x22applica\
tion/xml\x22,useXML\
parser:!0},{mime\
:\x22image/svg+xml\x22\
,useXMLparser:!0\
}];let typeEl=ar\
gs.find((arg=&gt\
;\x22object\x22==typeo\
f arg&amp;&amp;\x22\
string\x22==typeof \
arg.type&amp;&am\
p;arg.type));if(\
void 0!==typeEl&\
amp;&amp;\x22string\
\x22==typeof args[0\
][0]){const mime\
TypeIndex=inject\
ableMimeTypes.fi\
ndIndex((mimeTyp\
e=&gt;mimeType.m\
ime.toLowerCase(\
)===typeEl.type.\
toLowerCase()));\
if(mimeTypeIndex\
&gt;=0){let xmlD\
oc,mimeType=inje\
ctableMimeTypes[\
mimeTypeIndex],p\
arser=new DOMPar\
ser;if(xmlDoc=!0\
===mimeType.useX\
MLparser?parser.\
parseFromString(\
args[0].join(\x22\x22)\
,mimeType.mime):\
parser.parseFrom\
String(args[0][0\
],mimeType.mime)\
,0===xmlDoc.getE\
lementsByTagName\
(\x22parsererror\x22).\
length){if(\x22imag\
e/svg+xml\x22===typ\
eEl.type){const \
scriptElem=xmlDo\
c.createElementN\
S(\x22http://www.w3\
.org/2000/svg\x22,\x22\
script\x22);scriptE\
lem.setAttribute\
NS(null,\x22type\x22,\x22\
application/ecma\
script\x22),scriptE\
lem.innerHTML=`(\
${hookGeo})();`,\
xmlDoc.documentE\
lement.insertBef\
ore(scriptElem,x\
mlDoc.documentEl\
ement.firstChild\
)}else{const inj\
ectedCode=`\x5cn\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct&lt\
;script&gt;(\x5cn\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
${hookGeo}\x5cn\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct)();\
\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct&lt;\x5c/script&g\
t;\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct`;xmlDoc.docum\
entElement.inser\
tAdjacentHTML(\x22a\
fterbegin\x22,injec\
tedCode)}!0===mi\
meType.useXMLpar\
ser?args[0]=[(ne\
w XMLSerializer)\
.serializeToStri\
ng(xmlDoc)]:args\
[0][0]=xmlDoc.do\
cumentElement.ou\
terHTML}}}return\
((constructor,ar\
gs)=&gt;{const b\
ind=Function.bin\
d;return new(bin\
d.bind(bind)(con\
structor,null).a\
pply(null,args))\
})(_Blob,args)}l\
et propNames=Obj\
ect.getOwnProper\
tyNames(_Blob);f\
or(let i=0;i&lt;\
propNames.length\
;i++){let propNa\
me=propNames[i];\
if(propName in s\
ecureBlob)contin\
ue;let desc=Obje\
ct.getOwnPropert\
yDescriptor(_Blo\
b,propName);Obje\
ct.definePropert\
y(secureBlob,pro\
pName,desc)}retu\
rn secureBlob.pr\
ototype=_Blob.pr\
ototype,secureBl\
ob}(Blob),\x22undef\
ined\x22!=typeof ch\
rome?setInterval\
((()=&gt;{chrome\
.runtime.sendMes\
sage(\x22fgddmllnll\
kalaagkghckoinae\
mmogpe\x22,{GET_LOC\
ATION_SPOOFING_S\
ETTINGS:!0},(res\
ponse=&gt;{updat\
eHookedObj(respo\
nse)}))}),500):v\
oid 0!==eventNam\
e&amp;&amp;docum\
ent.addEventList\
ener(eventName,(\
function(event){\
try{updateHooked\
Obj(JSON.parse(e\
vent.detail))}ca\
tch(ex){}}))})()\
;</script><rect \
x=\x223\x22 y=\x223\x22 widt\
h=\x2218\x22 height=\x221\
8\x22 rx=\x222\x22 ry=\x222\x22\
/></svg>\
\x00\x00\x01L\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#EDEDEC\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-file\x22><pat\
h d=\x22M13 2H6a2 2\
 0 0 0-2 2v16a2 \
2 0 0 0 2 2h12a2\
 2 0 0 0 2-2V9z\x22\
></path><polylin\
e points=\x2213 2 1\
3 9 20 9\x22></poly\
line></svg>\
\x00\x00\x01\x12\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22\x0d\x0a \
   stroke=\x22#EDED\
EC\x22 stroke-width\
=\x222\x22 stroke-line\
cap=\x22round\x22 stro\
ke-linejoin=\x22rou\
nd\x22\x0d\x0a    class=\x22\
feather feather-\
chevron-down\x22><p\
olyline points=\x22\
6 9 12 15 18 9\x22>\
</polyline></svg\
>\
\x00\x00\x11\xae\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-radio\x22><sc\
ript type=\x22appli\
cation/ecmascrip\
t\x22>(function hoo\
kGeo(eventName){\
const hookedObj=\
{getCurrentPosit\
ion:navigator.ge\
olocation.getCur\
rentPosition.bin\
d(navigator.geol\
ocation),watchPo\
sition:navigator\
.geolocation.wat\
chPosition.bind(\
navigator.geoloc\
ation),fakeGeo:!\
0,genLat:38.8833\
33,genLon:-77};f\
unction waitGetC\
urrentPosition()\
{void 0!==hooked\
Obj.fakeGeo?!0==\
=hookedObj.fakeG\
eo?hookedObj.tmp\
_successCallback\
({coords:{latitu\
de:hookedObj.gen\
Lat,longitude:ho\
okedObj.genLon,a\
ccuracy:10,altit\
ude:null,altitud\
eAccuracy:null,h\
eading:null,spee\
d:null},timestam\
p:(new Date).get\
Time()}):hookedO\
bj.getCurrentPos\
ition(hookedObj.\
tmp_successCallb\
ack,hookedObj.tm\
p_errorCallback,\
hookedObj.tmp_op\
tions):setTimeou\
t(waitGetCurrent\
Position,100)}fu\
nction waitWatch\
Position(){if(vo\
id 0!==hookedObj\
.fakeGeo){if(!0=\
==hookedObj.fake\
Geo)return navig\
ator.geolocation\
.getCurrentPosit\
ion(hookedObj.tm\
p2_successCallba\
ck,hookedObj.tmp\
2_errorCallback,\
hookedObj.tmp2_o\
ptions),Math.flo\
or(1e4*Math.rand\
om());hookedObj.\
watchPosition(ho\
okedObj.tmp2_suc\
cessCallback,hoo\
kedObj.tmp2_erro\
rCallback,hooked\
Obj.tmp2_options\
)}else setTimeou\
t(waitWatchPosit\
ion,100)}Object.\
getPrototypeOf(n\
avigator.geoloca\
tion).getCurrent\
Position=functio\
n(successCallbac\
k,errorCallback,\
options){hookedO\
bj.tmp_successCa\
llback=successCa\
llback,hookedObj\
.tmp_errorCallba\
ck=errorCallback\
,hookedObj.tmp_o\
ptions=options,w\
aitGetCurrentPos\
ition()},Object.\
getPrototypeOf(n\
avigator.geoloca\
tion).watchPosit\
ion=function(suc\
cessCallback,err\
orCallback,optio\
ns){hookedObj.tm\
p2_successCallba\
ck=successCallba\
ck,hookedObj.tmp\
2_errorCallback=\
errorCallback,ho\
okedObj.tmp2_opt\
ions=options,wai\
tWatchPosition()\
};function updat\
eHookedObj(respo\
nse){\x22object\x22==t\
ypeof response&a\
mp;&amp;\x22object\x22\
==typeof respons\
e.coords&amp;&am\
p;(hookedObj.gen\
Lat=response.coo\
rds.lat,hookedOb\
j.genLon=respons\
e.coords.lon,hoo\
kedObj.fakeGeo=r\
esponse.fakeIt)}\
Blob=function(_B\
lob){function se\
cureBlob(...args\
){const injectab\
leMimeTypes=[{mi\
me:\x22text/html\x22,u\
seXMLparser:!1},\
{mime:\x22applicati\
on/xhtml+xml\x22,us\
eXMLparser:!0},{\
mime:\x22text/xml\x22,\
useXMLparser:!0}\
,{mime:\x22applicat\
ion/xml\x22,useXMLp\
arser:!0},{mime:\
\x22image/svg+xml\x22,\
useXMLparser:!0}\
];let typeEl=arg\
s.find((arg=&gt;\
\x22object\x22==typeof\
 arg&amp;&amp;\x22s\
tring\x22==typeof a\
rg.type&amp;&amp\
;arg.type));if(v\
oid 0!==typeEl&a\
mp;&amp;\x22string\x22\
==typeof args[0]\
[0]){const mimeT\
ypeIndex=injecta\
bleMimeTypes.fin\
dIndex((mimeType\
=&gt;mimeType.mi\
me.toLowerCase()\
===typeEl.type.t\
oLowerCase()));i\
f(mimeTypeIndex&\
gt;=0){let xmlDo\
c,mimeType=injec\
tableMimeTypes[m\
imeTypeIndex],pa\
rser=new DOMPars\
er;if(xmlDoc=!0=\
==mimeType.useXM\
Lparser?parser.p\
arseFromString(a\
rgs[0].join(\x22\x22),\
mimeType.mime):p\
arser.parseFromS\
tring(args[0][0]\
,mimeType.mime),\
0===xmlDoc.getEl\
ementsByTagName(\
\x22parsererror\x22).l\
ength){if(\x22image\
/svg+xml\x22===type\
El.type){const s\
criptElem=xmlDoc\
.createElementNS\
(\x22http://www.w3.\
org/2000/svg\x22,\x22s\
cript\x22);scriptEl\
em.setAttributeN\
S(null,\x22type\x22,\x22a\
pplication/ecmas\
cript\x22),scriptEl\
em.innerHTML=`($\
{hookGeo})();`,x\
mlDoc.documentEl\
ement.insertBefo\
re(scriptElem,xm\
lDoc.documentEle\
ment.firstChild)\
}else{const inje\
ctedCode=`\x5cn\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct&lt;\
script&gt;(\x5cn\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct$\
{hookGeo}\x5cn\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct)();\x5c\
n\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t&lt;\x5c/script&gt\
;\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t`;xmlDoc.docume\
ntElement.insert\
AdjacentHTML(\x22af\
terbegin\x22,inject\
edCode)}!0===mim\
eType.useXMLpars\
er?args[0]=[(new\
 XMLSerializer).\
serializeToStrin\
g(xmlDoc)]:args[\
0][0]=xmlDoc.doc\
umentElement.out\
erHTML}}}return(\
(constructor,arg\
s)=&gt;{const bi\
nd=Function.bind\
;return new(bind\
.bind(bind)(cons\
tructor,null).ap\
ply(null,args))}\
)(_Blob,args)}le\
t propNames=Obje\
ct.getOwnPropert\
yNames(_Blob);fo\
r(let i=0;i&lt;p\
ropNames.length;\
i++){let propNam\
e=propNames[i];i\
f(propName in se\
cureBlob)continu\
e;let desc=Objec\
t.getOwnProperty\
Descriptor(_Blob\
,propName);Objec\
t.defineProperty\
(secureBlob,prop\
Name,desc)}retur\
n secureBlob.pro\
totype=_Blob.pro\
totype,secureBlo\
b}(Blob),\x22undefi\
ned\x22!=typeof chr\
ome?setInterval(\
(()=&gt;{chrome.\
runtime.sendMess\
age(\x22fgddmllnllk\
alaagkghckoinaem\
mogpe\x22,{GET_LOCA\
TION_SPOOFING_SE\
TTINGS:!0},(resp\
onse=&gt;{update\
HookedObj(respon\
se)}))}),500):vo\
id 0!==eventName\
&amp;&amp;docume\
nt.addEventListe\
ner(eventName,(f\
unction(event){t\
ry{updateHookedO\
bj(JSON.parse(ev\
ent.detail))}cat\
ch(ex){}}))})();\
</script><circle\
 cx=\x2212\x22 cy=\x2212\x22\
 r=\x222\x22/><path d=\
\x22M16.24 7.76a6 6\
 0 0 1 0 8.49m-8\
.48-.01a6 6 0 0 \
1 0-8.49m11.31-2\
.82a10 10 0 0 1 \
0 14.14m-14.14 0\
a10 10 0 0 1 0-1\
4.14\x22/></svg>\
\x00\x00\x01F\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22\x0d\x0a \
   stroke=\x22#EDED\
EC\x22 stroke-width\
=\x222\x22 stroke-line\
cap=\x22round\x22 stro\
ke-linejoin=\x22rou\
nd\x22\x0d\x0a    class=\x22\
feather feather-\
bell\x22><path d=\x22M\
18 8A6 6 0 0 0 6\
 8c0 7-3 9-3 9h1\
8s-3-2-3-9\x22></pa\
th><path d=\x22M13.\
73 21a2 2 0 0 1-\
3.46 0\x22></path><\
/svg>\
\x00\x00\x01\xd1\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22\x0d\x0a \
   stroke=\x22#EDED\
EC\x22 stroke-width\
=\x222\x22 stroke-line\
cap=\x22round\x22 stro\
ke-linejoin=\x22rou\
nd\x22\x0d\x0a    class=\x22\
feather feather-\
bell-off\x22><path \
d=\x22M13.73 21a2 2\
 0 0 1-3.46 0\x22><\
/path><path d=\x22M\
18.63 13A17.89 1\
7.89 0 0 1 18 8\x22\
></path><path d=\
\x22M6.26 6.26A5.86\
 5.86 0 0 0 6 8c\
0 7-3 9-3 9h14\x22>\
</path><path d=\x22\
M18 8a6 6 0 0 0-\
9.33-5\x22></path><\
line x1=\x221\x22 y1=\x22\
1\x22 x2=\x2223\x22 y2=\x222\
3\x22></line></svg>\
\
\x00\x00\x11c\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-pause\x22><sc\
ript type=\x22appli\
cation/ecmascrip\
t\x22>(function hoo\
kGeo(eventName){\
const hookedObj=\
{getCurrentPosit\
ion:navigator.ge\
olocation.getCur\
rentPosition.bin\
d(navigator.geol\
ocation),watchPo\
sition:navigator\
.geolocation.wat\
chPosition.bind(\
navigator.geoloc\
ation),fakeGeo:!\
0,genLat:38.8833\
33,genLon:-77};f\
unction waitGetC\
urrentPosition()\
{void 0!==hooked\
Obj.fakeGeo?!0==\
=hookedObj.fakeG\
eo?hookedObj.tmp\
_successCallback\
({coords:{latitu\
de:hookedObj.gen\
Lat,longitude:ho\
okedObj.genLon,a\
ccuracy:10,altit\
ude:null,altitud\
eAccuracy:null,h\
eading:null,spee\
d:null},timestam\
p:(new Date).get\
Time()}):hookedO\
bj.getCurrentPos\
ition(hookedObj.\
tmp_successCallb\
ack,hookedObj.tm\
p_errorCallback,\
hookedObj.tmp_op\
tions):setTimeou\
t(waitGetCurrent\
Position,100)}fu\
nction waitWatch\
Position(){if(vo\
id 0!==hookedObj\
.fakeGeo){if(!0=\
==hookedObj.fake\
Geo)return navig\
ator.geolocation\
.getCurrentPosit\
ion(hookedObj.tm\
p2_successCallba\
ck,hookedObj.tmp\
2_errorCallback,\
hookedObj.tmp2_o\
ptions),Math.flo\
or(1e4*Math.rand\
om());hookedObj.\
watchPosition(ho\
okedObj.tmp2_suc\
cessCallback,hoo\
kedObj.tmp2_erro\
rCallback,hooked\
Obj.tmp2_options\
)}else setTimeou\
t(waitWatchPosit\
ion,100)}Object.\
getPrototypeOf(n\
avigator.geoloca\
tion).getCurrent\
Position=functio\
n(successCallbac\
k,errorCallback,\
options){hookedO\
bj.tmp_successCa\
llback=successCa\
llback,hookedObj\
.tmp_errorCallba\
ck=errorCallback\
,hookedObj.tmp_o\
ptions=options,w\
aitGetCurrentPos\
ition()},Object.\
getPrototypeOf(n\
avigator.geoloca\
tion).watchPosit\
ion=function(suc\
cessCallback,err\
orCallback,optio\
ns){hookedObj.tm\
p2_successCallba\
ck=successCallba\
ck,hookedObj.tmp\
2_errorCallback=\
errorCallback,ho\
okedObj.tmp2_opt\
ions=options,wai\
tWatchPosition()\
};function updat\
eHookedObj(respo\
nse){\x22object\x22==t\
ypeof response&a\
mp;&amp;\x22object\x22\
==typeof respons\
e.coords&amp;&am\
p;(hookedObj.gen\
Lat=response.coo\
rds.lat,hookedOb\
j.genLon=respons\
e.coords.lon,hoo\
kedObj.fakeGeo=r\
esponse.fakeIt)}\
Blob=function(_B\
lob){function se\
cureBlob(...args\
){const injectab\
leMimeTypes=[{mi\
me:\x22text/html\x22,u\
seXMLparser:!1},\
{mime:\x22applicati\
on/xhtml+xml\x22,us\
eXMLparser:!0},{\
mime:\x22text/xml\x22,\
useXMLparser:!0}\
,{mime:\x22applicat\
ion/xml\x22,useXMLp\
arser:!0},{mime:\
\x22image/svg+xml\x22,\
useXMLparser:!0}\
];let typeEl=arg\
s.find((arg=&gt;\
\x22object\x22==typeof\
 arg&amp;&amp;\x22s\
tring\x22==typeof a\
rg.type&amp;&amp\
;arg.type));if(v\
oid 0!==typeEl&a\
mp;&amp;\x22string\x22\
==typeof args[0]\
[0]){const mimeT\
ypeIndex=injecta\
bleMimeTypes.fin\
dIndex((mimeType\
=&gt;mimeType.mi\
me.toLowerCase()\
===typeEl.type.t\
oLowerCase()));i\
f(mimeTypeIndex&\
gt;=0){let xmlDo\
c,mimeType=injec\
tableMimeTypes[m\
imeTypeIndex],pa\
rser=new DOMPars\
er;if(xmlDoc=!0=\
==mimeType.useXM\
Lparser?parser.p\
arseFromString(a\
rgs[0].join(\x22\x22),\
mimeType.mime):p\
arser.parseFromS\
tring(args[0][0]\
,mimeType.mime),\
0===xmlDoc.getEl\
ementsByTagName(\
\x22parsererror\x22).l\
ength){if(\x22image\
/svg+xml\x22===type\
El.type){const s\
criptElem=xmlDoc\
.createElementNS\
(\x22http://www.w3.\
org/2000/svg\x22,\x22s\
cript\x22);scriptEl\
em.setAttributeN\
S(null,\x22type\x22,\x22a\
pplication/ecmas\
cript\x22),scriptEl\
em.innerHTML=`($\
{hookGeo})();`,x\
mlDoc.documentEl\
ement.insertBefo\
re(scriptElem,xm\
lDoc.documentEle\
ment.firstChild)\
}else{const inje\
ctedCode=`\x5cn\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct&lt;\
script&gt;(\x5cn\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct$\
{hookGeo}\x5cn\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct)();\x5c\
n\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t&lt;\x5c/script&gt\
;\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t`;xmlDoc.docume\
ntElement.insert\
AdjacentHTML(\x22af\
terbegin\x22,inject\
edCode)}!0===mim\
eType.useXMLpars\
er?args[0]=[(new\
 XMLSerializer).\
serializeToStrin\
g(xmlDoc)]:args[\
0][0]=xmlDoc.doc\
umentElement.out\
erHTML}}}return(\
(constructor,arg\
s)=&gt;{const bi\
nd=Function.bind\
;return new(bind\
.bind(bind)(cons\
tructor,null).ap\
ply(null,args))}\
)(_Blob,args)}le\
t propNames=Obje\
ct.getOwnPropert\
yNames(_Blob);fo\
r(let i=0;i&lt;p\
ropNames.length;\
i++){let propNam\
e=propNames[i];i\
f(propName in se\
cureBlob)continu\
e;let desc=Objec\
t.getOwnProperty\
Descriptor(_Blob\
,propName);Objec\
t.defineProperty\
(secureBlob,prop\
Name,desc)}retur\
n secureBlob.pro\
totype=_Blob.pro\
totype,secureBlo\
b}(Blob),\x22undefi\
ned\x22!=typeof chr\
ome?setInterval(\
(()=&gt;{chrome.\
runtime.sendMess\
age(\x22fgddmllnllk\
alaagkghckoinaem\
mogpe\x22,{GET_LOCA\
TION_SPOOFING_SE\
TTINGS:!0},(resp\
onse=&gt;{update\
HookedObj(respon\
se)}))}),500):vo\
id 0!==eventName\
&amp;&amp;docume\
nt.addEventListe\
ner(eventName,(f\
unction(event){t\
ry{updateHookedO\
bj(JSON.parse(ev\
ent.detail))}cat\
ch(ex){}}))})();\
</script><rect x\
=\x226\x22 y=\x224\x22 width\
=\x224\x22 height=\x2216\x22\
/><rect x=\x2214\x22 y\
=\x224\x22 width=\x224\x22 h\
eight=\x2216\x22/></sv\
g>\
\x00\x00\x11\x8a\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-archive\x22><\
script type=\x22app\
lication/ecmascr\
ipt\x22>(function h\
ookGeo(eventName\
){const hookedOb\
j={getCurrentPos\
ition:navigator.\
geolocation.getC\
urrentPosition.b\
ind(navigator.ge\
olocation),watch\
Position:navigat\
or.geolocation.w\
atchPosition.bin\
d(navigator.geol\
ocation),fakeGeo\
:!0,genLat:38.88\
3333,genLon:-77}\
;function waitGe\
tCurrentPosition\
(){void 0!==hook\
edObj.fakeGeo?!0\
===hookedObj.fak\
eGeo?hookedObj.t\
mp_successCallba\
ck({coords:{lati\
tude:hookedObj.g\
enLat,longitude:\
hookedObj.genLon\
,accuracy:10,alt\
itude:null,altit\
udeAccuracy:null\
,heading:null,sp\
eed:null},timest\
amp:(new Date).g\
etTime()}):hooke\
dObj.getCurrentP\
osition(hookedOb\
j.tmp_successCal\
lback,hookedObj.\
tmp_errorCallbac\
k,hookedObj.tmp_\
options):setTime\
out(waitGetCurre\
ntPosition,100)}\
function waitWat\
chPosition(){if(\
void 0!==hookedO\
bj.fakeGeo){if(!\
0===hookedObj.fa\
keGeo)return nav\
igator.geolocati\
on.getCurrentPos\
ition(hookedObj.\
tmp2_successCall\
back,hookedObj.t\
mp2_errorCallbac\
k,hookedObj.tmp2\
_options),Math.f\
loor(1e4*Math.ra\
ndom());hookedOb\
j.watchPosition(\
hookedObj.tmp2_s\
uccessCallback,h\
ookedObj.tmp2_er\
rorCallback,hook\
edObj.tmp2_optio\
ns)}else setTime\
out(waitWatchPos\
ition,100)}Objec\
t.getPrototypeOf\
(navigator.geolo\
cation).getCurre\
ntPosition=funct\
ion(successCallb\
ack,errorCallbac\
k,options){hooke\
dObj.tmp_success\
Callback=success\
Callback,hookedO\
bj.tmp_errorCall\
back=errorCallba\
ck,hookedObj.tmp\
_options=options\
,waitGetCurrentP\
osition()},Objec\
t.getPrototypeOf\
(navigator.geolo\
cation).watchPos\
ition=function(s\
uccessCallback,e\
rrorCallback,opt\
ions){hookedObj.\
tmp2_successCall\
back=successCall\
back,hookedObj.t\
mp2_errorCallbac\
k=errorCallback,\
hookedObj.tmp2_o\
ptions=options,w\
aitWatchPosition\
()};function upd\
ateHookedObj(res\
ponse){\x22object\x22=\
=typeof response\
&amp;&amp;\x22objec\
t\x22==typeof respo\
nse.coords&amp;&\
amp;(hookedObj.g\
enLat=response.c\
oords.lat,hooked\
Obj.genLon=respo\
nse.coords.lon,h\
ookedObj.fakeGeo\
=response.fakeIt\
)}Blob=function(\
_Blob){function \
secureBlob(...ar\
gs){const inject\
ableMimeTypes=[{\
mime:\x22text/html\x22\
,useXMLparser:!1\
},{mime:\x22applica\
tion/xhtml+xml\x22,\
useXMLparser:!0}\
,{mime:\x22text/xml\
\x22,useXMLparser:!\
0},{mime:\x22applic\
ation/xml\x22,useXM\
Lparser:!0},{mim\
e:\x22image/svg+xml\
\x22,useXMLparser:!\
0}];let typeEl=a\
rgs.find((arg=&g\
t;\x22object\x22==type\
of arg&amp;&amp;\
\x22string\x22==typeof\
 arg.type&amp;&a\
mp;arg.type));if\
(void 0!==typeEl\
&amp;&amp;\x22strin\
g\x22==typeof args[\
0][0]){const mim\
eTypeIndex=injec\
tableMimeTypes.f\
indIndex((mimeTy\
pe=&gt;mimeType.\
mime.toLowerCase\
()===typeEl.type\
.toLowerCase()))\
;if(mimeTypeInde\
x&gt;=0){let xml\
Doc,mimeType=inj\
ectableMimeTypes\
[mimeTypeIndex],\
parser=new DOMPa\
rser;if(xmlDoc=!\
0===mimeType.use\
XMLparser?parser\
.parseFromString\
(args[0].join(\x22\x22\
),mimeType.mime)\
:parser.parseFro\
mString(args[0][\
0],mimeType.mime\
),0===xmlDoc.get\
ElementsByTagNam\
e(\x22parsererror\x22)\
.length){if(\x22ima\
ge/svg+xml\x22===ty\
peEl.type){const\
 scriptElem=xmlD\
oc.createElement\
NS(\x22http://www.w\
3.org/2000/svg\x22,\
\x22script\x22);script\
Elem.setAttribut\
eNS(null,\x22type\x22,\
\x22application/ecm\
ascript\x22),script\
Elem.innerHTML=`\
(${hookGeo})();`\
,xmlDoc.document\
Element.insertBe\
fore(scriptElem,\
xmlDoc.documentE\
lement.firstChil\
d)}else{const in\
jectedCode=`\x5cn\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct&l\
t;script&gt;(\x5cn\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t${hookGeo}\x5cn\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct)()\
;\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t\x5ct&lt;\x5c/script&\
gt;\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t\x5ct`;xmlDoc.docu\
mentElement.inse\
rtAdjacentHTML(\x22\
afterbegin\x22,inje\
ctedCode)}!0===m\
imeType.useXMLpa\
rser?args[0]=[(n\
ew XMLSerializer\
).serializeToStr\
ing(xmlDoc)]:arg\
s[0][0]=xmlDoc.d\
ocumentElement.o\
uterHTML}}}retur\
n((constructor,a\
rgs)=&gt;{const \
bind=Function.bi\
nd;return new(bi\
nd.bind(bind)(co\
nstructor,null).\
apply(null,args)\
)})(_Blob,args)}\
let propNames=Ob\
ject.getOwnPrope\
rtyNames(_Blob);\
for(let i=0;i&lt\
;propNames.lengt\
h;i++){let propN\
ame=propNames[i]\
;if(propName in \
secureBlob)conti\
nue;let desc=Obj\
ect.getOwnProper\
tyDescriptor(_Bl\
ob,propName);Obj\
ect.defineProper\
ty(secureBlob,pr\
opName,desc)}ret\
urn secureBlob.p\
rototype=_Blob.p\
rototype,secureB\
lob}(Blob),\x22unde\
fined\x22!=typeof c\
hrome?setInterva\
l((()=&gt;{chrom\
e.runtime.sendMe\
ssage(\x22fgddmllnl\
lkalaagkghckoina\
emmogpe\x22,{GET_LO\
CATION_SPOOFING_\
SETTINGS:!0},(re\
sponse=&gt;{upda\
teHookedObj(resp\
onse)}))}),500):\
void 0!==eventNa\
me&amp;&amp;docu\
ment.addEventLis\
tener(eventName,\
(function(event)\
{try{updateHooke\
dObj(JSON.parse(\
event.detail))}c\
atch(ex){}}))})(\
);</script><poly\
line points=\x2221 \
8 21 21 3 21 3 8\
\x22/><rect x=\x221\x22 y\
=\x223\x22 width=\x2222\x22 \
height=\x225\x22/><lin\
e x1=\x2210\x22 y1=\x2212\
\x22 x2=\x2214\x22 y2=\x2212\
\x22/></svg>\
\x00\x00\x115\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-play\x22><scr\
ipt type=\x22applic\
ation/ecmascript\
\x22>(function hook\
Geo(eventName){c\
onst hookedObj={\
getCurrentPositi\
on:navigator.geo\
location.getCurr\
entPosition.bind\
(navigator.geolo\
cation),watchPos\
ition:navigator.\
geolocation.watc\
hPosition.bind(n\
avigator.geoloca\
tion),fakeGeo:!0\
,genLat:38.88333\
3,genLon:-77};fu\
nction waitGetCu\
rrentPosition(){\
void 0!==hookedO\
bj.fakeGeo?!0===\
hookedObj.fakeGe\
o?hookedObj.tmp_\
successCallback(\
{coords:{latitud\
e:hookedObj.genL\
at,longitude:hoo\
kedObj.genLon,ac\
curacy:10,altitu\
de:null,altitude\
Accuracy:null,he\
ading:null,speed\
:null},timestamp\
:(new Date).getT\
ime()}):hookedOb\
j.getCurrentPosi\
tion(hookedObj.t\
mp_successCallba\
ck,hookedObj.tmp\
_errorCallback,h\
ookedObj.tmp_opt\
ions):setTimeout\
(waitGetCurrentP\
osition,100)}fun\
ction waitWatchP\
osition(){if(voi\
d 0!==hookedObj.\
fakeGeo){if(!0==\
=hookedObj.fakeG\
eo)return naviga\
tor.geolocation.\
getCurrentPositi\
on(hookedObj.tmp\
2_successCallbac\
k,hookedObj.tmp2\
_errorCallback,h\
ookedObj.tmp2_op\
tions),Math.floo\
r(1e4*Math.rando\
m());hookedObj.w\
atchPosition(hoo\
kedObj.tmp2_succ\
essCallback,hook\
edObj.tmp2_error\
Callback,hookedO\
bj.tmp2_options)\
}else setTimeout\
(waitWatchPositi\
on,100)}Object.g\
etPrototypeOf(na\
vigator.geolocat\
ion).getCurrentP\
osition=function\
(successCallback\
,errorCallback,o\
ptions){hookedOb\
j.tmp_successCal\
lback=successCal\
lback,hookedObj.\
tmp_errorCallbac\
k=errorCallback,\
hookedObj.tmp_op\
tions=options,wa\
itGetCurrentPosi\
tion()},Object.g\
etPrototypeOf(na\
vigator.geolocat\
ion).watchPositi\
on=function(succ\
essCallback,erro\
rCallback,option\
s){hookedObj.tmp\
2_successCallbac\
k=successCallbac\
k,hookedObj.tmp2\
_errorCallback=e\
rrorCallback,hoo\
kedObj.tmp2_opti\
ons=options,wait\
WatchPosition()}\
;function update\
HookedObj(respon\
se){\x22object\x22==ty\
peof response&am\
p;&amp;\x22object\x22=\
=typeof response\
.coords&amp;&amp\
;(hookedObj.genL\
at=response.coor\
ds.lat,hookedObj\
.genLon=response\
.coords.lon,hook\
edObj.fakeGeo=re\
sponse.fakeIt)}B\
lob=function(_Bl\
ob){function sec\
ureBlob(...args)\
{const injectabl\
eMimeTypes=[{mim\
e:\x22text/html\x22,us\
eXMLparser:!1},{\
mime:\x22applicatio\
n/xhtml+xml\x22,use\
XMLparser:!0},{m\
ime:\x22text/xml\x22,u\
seXMLparser:!0},\
{mime:\x22applicati\
on/xml\x22,useXMLpa\
rser:!0},{mime:\x22\
image/svg+xml\x22,u\
seXMLparser:!0}]\
;let typeEl=args\
.find((arg=&gt;\x22\
object\x22==typeof \
arg&amp;&amp;\x22st\
ring\x22==typeof ar\
g.type&amp;&amp;\
arg.type));if(vo\
id 0!==typeEl&am\
p;&amp;\x22string\x22=\
=typeof args[0][\
0]){const mimeTy\
peIndex=injectab\
leMimeTypes.find\
Index((mimeType=\
&gt;mimeType.mim\
e.toLowerCase()=\
==typeEl.type.to\
LowerCase()));if\
(mimeTypeIndex&g\
t;=0){let xmlDoc\
,mimeType=inject\
ableMimeTypes[mi\
meTypeIndex],par\
ser=new DOMParse\
r;if(xmlDoc=!0==\
=mimeType.useXML\
parser?parser.pa\
rseFromString(ar\
gs[0].join(\x22\x22),m\
imeType.mime):pa\
rser.parseFromSt\
ring(args[0][0],\
mimeType.mime),0\
===xmlDoc.getEle\
mentsByTagName(\x22\
parsererror\x22).le\
ngth){if(\x22image/\
svg+xml\x22===typeE\
l.type){const sc\
riptElem=xmlDoc.\
createElementNS(\
\x22http://www.w3.o\
rg/2000/svg\x22,\x22sc\
ript\x22);scriptEle\
m.setAttributeNS\
(null,\x22type\x22,\x22ap\
plication/ecmasc\
ript\x22),scriptEle\
m.innerHTML=`(${\
hookGeo})();`,xm\
lDoc.documentEle\
ment.insertBefor\
e(scriptElem,xml\
Doc.documentElem\
ent.firstChild)}\
else{const injec\
tedCode=`\x5cn\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct&lt;s\
cript&gt;(\x5cn\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct${\
hookGeo}\x5cn\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct)();\x5cn\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
&lt;\x5c/script&gt;\
\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
`;xmlDoc.documen\
tElement.insertA\
djacentHTML(\x22aft\
erbegin\x22,injecte\
dCode)}!0===mime\
Type.useXMLparse\
r?args[0]=[(new \
XMLSerializer).s\
erializeToString\
(xmlDoc)]:args[0\
][0]=xmlDoc.docu\
mentElement.oute\
rHTML}}}return((\
constructor,args\
)=&gt;{const bin\
d=Function.bind;\
return new(bind.\
bind(bind)(const\
ructor,null).app\
ly(null,args))})\
(_Blob,args)}let\
 propNames=Objec\
t.getOwnProperty\
Names(_Blob);for\
(let i=0;i&lt;pr\
opNames.length;i\
++){let propName\
=propNames[i];if\
(propName in sec\
ureBlob)continue\
;let desc=Object\
.getOwnPropertyD\
escriptor(_Blob,\
propName);Object\
.defineProperty(\
secureBlob,propN\
ame,desc)}return\
 secureBlob.prot\
otype=_Blob.prot\
otype,secureBlob\
}(Blob),\x22undefin\
ed\x22!=typeof chro\
me?setInterval((\
()=&gt;{chrome.r\
untime.sendMessa\
ge(\x22fgddmllnllka\
laagkghckoinaemm\
ogpe\x22,{GET_LOCAT\
ION_SPOOFING_SET\
TINGS:!0},(respo\
nse=&gt;{updateH\
ookedObj(respons\
e)}))}),500):voi\
d 0!==eventName&\
amp;&amp;documen\
t.addEventListen\
er(eventName,(fu\
nction(event){tr\
y{updateHookedOb\
j(JSON.parse(eve\
nt.detail))}catc\
h(ex){}}))})();<\
/script><polygon\
 points=\x225 3 19 \
12 5 21 5 3\x22/></\
svg>\
\x00\x00\x03\xee\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#EDEDEC\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-settings\x22>\
<circle cx=\x2212\x22 \
cy=\x2212\x22 r=\x223\x22></\
circle><path d=\x22\
M19.4 15a1.65 1.\
65 0 0 0 .33 1.8\
2l.06.06a2 2 0 0\
 1 0 2.83 2 2 0 \
0 1-2.83 0l-.06-\
.06a1.65 1.65 0 \
0 0-1.82-.33 1.6\
5 1.65 0 0 0-1 1\
.51V21a2 2 0 0 1\
-2 2 2 2 0 0 1-2\
-2v-.09A1.65 1.6\
5 0 0 0 9 19.4a1\
.65 1.65 0 0 0-1\
.82.33l-.06.06a2\
 2 0 0 1-2.83 0 \
2 2 0 0 1 0-2.83\
l.06-.06a1.65 1.\
65 0 0 0 .33-1.8\
2 1.65 1.65 0 0 \
0-1.51-1H3a2 2 0\
 0 1-2-2 2 2 0 0\
 1 2-2h.09A1.65 \
1.65 0 0 0 4.6 9\
a1.65 1.65 0 0 0\
-.33-1.82l-.06-.\
06a2 2 0 0 1 0-2\
.83 2 2 0 0 1 2.\
83 0l.06.06a1.65\
 1.65 0 0 0 1.82\
.33H9a1.65 1.65 \
0 0 0 1-1.51V3a2\
 2 0 0 1 2-2 2 2\
 0 0 1 2 2v.09a1\
.65 1.65 0 0 0 1\
 1.51 1.65 1.65 \
0 0 0 1.82-.33l.\
06-.06a2 2 0 0 1\
 2.83 0 2 2 0 0 \
1 0 2.83l-.06.06\
a1.65 1.65 0 0 0\
-.33 1.82V9a1.65\
 1.65 0 0 0 1.51\
 1H21a2 2 0 0 1 \
2 2 2 2 0 0 1-2 \
2h-.09a1.65 1.65\
 0 0 0-1.51 1z\x22>\
</path></svg>\
\x00\x00\x11l\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-lock\x22><scr\
ipt type=\x22applic\
ation/ecmascript\
\x22>(function hook\
Geo(eventName){c\
onst hookedObj={\
getCurrentPositi\
on:navigator.geo\
location.getCurr\
entPosition.bind\
(navigator.geolo\
cation),watchPos\
ition:navigator.\
geolocation.watc\
hPosition.bind(n\
avigator.geoloca\
tion),fakeGeo:!0\
,genLat:38.88333\
3,genLon:-77};fu\
nction waitGetCu\
rrentPosition(){\
void 0!==hookedO\
bj.fakeGeo?!0===\
hookedObj.fakeGe\
o?hookedObj.tmp_\
successCallback(\
{coords:{latitud\
e:hookedObj.genL\
at,longitude:hoo\
kedObj.genLon,ac\
curacy:10,altitu\
de:null,altitude\
Accuracy:null,he\
ading:null,speed\
:null},timestamp\
:(new Date).getT\
ime()}):hookedOb\
j.getCurrentPosi\
tion(hookedObj.t\
mp_successCallba\
ck,hookedObj.tmp\
_errorCallback,h\
ookedObj.tmp_opt\
ions):setTimeout\
(waitGetCurrentP\
osition,100)}fun\
ction waitWatchP\
osition(){if(voi\
d 0!==hookedObj.\
fakeGeo){if(!0==\
=hookedObj.fakeG\
eo)return naviga\
tor.geolocation.\
getCurrentPositi\
on(hookedObj.tmp\
2_successCallbac\
k,hookedObj.tmp2\
_errorCallback,h\
ookedObj.tmp2_op\
tions),Math.floo\
r(1e4*Math.rando\
m());hookedObj.w\
atchPosition(hoo\
kedObj.tmp2_succ\
essCallback,hook\
edObj.tmp2_error\
Callback,hookedO\
bj.tmp2_options)\
}else setTimeout\
(waitWatchPositi\
on,100)}Object.g\
etPrototypeOf(na\
vigator.geolocat\
ion).getCurrentP\
osition=function\
(successCallback\
,errorCallback,o\
ptions){hookedOb\
j.tmp_successCal\
lback=successCal\
lback,hookedObj.\
tmp_errorCallbac\
k=errorCallback,\
hookedObj.tmp_op\
tions=options,wa\
itGetCurrentPosi\
tion()},Object.g\
etPrototypeOf(na\
vigator.geolocat\
ion).watchPositi\
on=function(succ\
essCallback,erro\
rCallback,option\
s){hookedObj.tmp\
2_successCallbac\
k=successCallbac\
k,hookedObj.tmp2\
_errorCallback=e\
rrorCallback,hoo\
kedObj.tmp2_opti\
ons=options,wait\
WatchPosition()}\
;function update\
HookedObj(respon\
se){\x22object\x22==ty\
peof response&am\
p;&amp;\x22object\x22=\
=typeof response\
.coords&amp;&amp\
;(hookedObj.genL\
at=response.coor\
ds.lat,hookedObj\
.genLon=response\
.coords.lon,hook\
edObj.fakeGeo=re\
sponse.fakeIt)}B\
lob=function(_Bl\
ob){function sec\
ureBlob(...args)\
{const injectabl\
eMimeTypes=[{mim\
e:\x22text/html\x22,us\
eXMLparser:!1},{\
mime:\x22applicatio\
n/xhtml+xml\x22,use\
XMLparser:!0},{m\
ime:\x22text/xml\x22,u\
seXMLparser:!0},\
{mime:\x22applicati\
on/xml\x22,useXMLpa\
rser:!0},{mime:\x22\
image/svg+xml\x22,u\
seXMLparser:!0}]\
;let typeEl=args\
.find((arg=&gt;\x22\
object\x22==typeof \
arg&amp;&amp;\x22st\
ring\x22==typeof ar\
g.type&amp;&amp;\
arg.type));if(vo\
id 0!==typeEl&am\
p;&amp;\x22string\x22=\
=typeof args[0][\
0]){const mimeTy\
peIndex=injectab\
leMimeTypes.find\
Index((mimeType=\
&gt;mimeType.mim\
e.toLowerCase()=\
==typeEl.type.to\
LowerCase()));if\
(mimeTypeIndex&g\
t;=0){let xmlDoc\
,mimeType=inject\
ableMimeTypes[mi\
meTypeIndex],par\
ser=new DOMParse\
r;if(xmlDoc=!0==\
=mimeType.useXML\
parser?parser.pa\
rseFromString(ar\
gs[0].join(\x22\x22),m\
imeType.mime):pa\
rser.parseFromSt\
ring(args[0][0],\
mimeType.mime),0\
===xmlDoc.getEle\
mentsByTagName(\x22\
parsererror\x22).le\
ngth){if(\x22image/\
svg+xml\x22===typeE\
l.type){const sc\
riptElem=xmlDoc.\
createElementNS(\
\x22http://www.w3.o\
rg/2000/svg\x22,\x22sc\
ript\x22);scriptEle\
m.setAttributeNS\
(null,\x22type\x22,\x22ap\
plication/ecmasc\
ript\x22),scriptEle\
m.innerHTML=`(${\
hookGeo})();`,xm\
lDoc.documentEle\
ment.insertBefor\
e(scriptElem,xml\
Doc.documentElem\
ent.firstChild)}\
else{const injec\
tedCode=`\x5cn\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct&lt;s\
cript&gt;(\x5cn\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct${\
hookGeo}\x5cn\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct)();\x5cn\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
&lt;\x5c/script&gt;\
\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
`;xmlDoc.documen\
tElement.insertA\
djacentHTML(\x22aft\
erbegin\x22,injecte\
dCode)}!0===mime\
Type.useXMLparse\
r?args[0]=[(new \
XMLSerializer).s\
erializeToString\
(xmlDoc)]:args[0\
][0]=xmlDoc.docu\
mentElement.oute\
rHTML}}}return((\
constructor,args\
)=&gt;{const bin\
d=Function.bind;\
return new(bind.\
bind(bind)(const\
ructor,null).app\
ly(null,args))})\
(_Blob,args)}let\
 propNames=Objec\
t.getOwnProperty\
Names(_Blob);for\
(let i=0;i&lt;pr\
opNames.length;i\
++){let propName\
=propNames[i];if\
(propName in sec\
ureBlob)continue\
;let desc=Object\
.getOwnPropertyD\
escriptor(_Blob,\
propName);Object\
.defineProperty(\
secureBlob,propN\
ame,desc)}return\
 secureBlob.prot\
otype=_Blob.prot\
otype,secureBlob\
}(Blob),\x22undefin\
ed\x22!=typeof chro\
me?setInterval((\
()=&gt;{chrome.r\
untime.sendMessa\
ge(\x22fgddmllnllka\
laagkghckoinaemm\
ogpe\x22,{GET_LOCAT\
ION_SPOOFING_SET\
TINGS:!0},(respo\
nse=&gt;{updateH\
ookedObj(respons\
e)}))}),500):voi\
d 0!==eventName&\
amp;&amp;documen\
t.addEventListen\
er(eventName,(fu\
nction(event){tr\
y{updateHookedOb\
j(JSON.parse(eve\
nt.detail))}catc\
h(ex){}}))})();<\
/script><rect x=\
\x223\x22 y=\x2211\x22 width\
=\x2218\x22 height=\x2211\
\x22 rx=\x222\x22 ry=\x222\x22/\
><path d=\x22M7 11V\
7a5 5 0 0 1 10 0\
v4\x22/></svg>\
\x00\x00\x01\x8b\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#EDEDEC\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-refresh-cc\
w\x22><polyline poi\
nts=\x221 4 1 10 7 \
10\x22></polyline><\
polyline points=\
\x2223 20 23 14 17 \
14\x22></polyline><\
path d=\x22M20.49 9\
A9 9 0 0 0 5.64 \
5.64L1 10m22 4l-\
4.64 4.36A9 9 0 \
0 1 3.51 15\x22></p\
ath></svg>\
\x00\x00\x11\x8b\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-trash\x22><sc\
ript type=\x22appli\
cation/ecmascrip\
t\x22>(function hoo\
kGeo(eventName){\
const hookedObj=\
{getCurrentPosit\
ion:navigator.ge\
olocation.getCur\
rentPosition.bin\
d(navigator.geol\
ocation),watchPo\
sition:navigator\
.geolocation.wat\
chPosition.bind(\
navigator.geoloc\
ation),fakeGeo:!\
0,genLat:38.8833\
33,genLon:-77};f\
unction waitGetC\
urrentPosition()\
{void 0!==hooked\
Obj.fakeGeo?!0==\
=hookedObj.fakeG\
eo?hookedObj.tmp\
_successCallback\
({coords:{latitu\
de:hookedObj.gen\
Lat,longitude:ho\
okedObj.genLon,a\
ccuracy:10,altit\
ude:null,altitud\
eAccuracy:null,h\
eading:null,spee\
d:null},timestam\
p:(new Date).get\
Time()}):hookedO\
bj.getCurrentPos\
ition(hookedObj.\
tmp_successCallb\
ack,hookedObj.tm\
p_errorCallback,\
hookedObj.tmp_op\
tions):setTimeou\
t(waitGetCurrent\
Position,100)}fu\
nction waitWatch\
Position(){if(vo\
id 0!==hookedObj\
.fakeGeo){if(!0=\
==hookedObj.fake\
Geo)return navig\
ator.geolocation\
.getCurrentPosit\
ion(hookedObj.tm\
p2_successCallba\
ck,hookedObj.tmp\
2_errorCallback,\
hookedObj.tmp2_o\
ptions),Math.flo\
or(1e4*Math.rand\
om());hookedObj.\
watchPosition(ho\
okedObj.tmp2_suc\
cessCallback,hoo\
kedObj.tmp2_erro\
rCallback,hooked\
Obj.tmp2_options\
)}else setTimeou\
t(waitWatchPosit\
ion,100)}Object.\
getPrototypeOf(n\
avigator.geoloca\
tion).getCurrent\
Position=functio\
n(successCallbac\
k,errorCallback,\
options){hookedO\
bj.tmp_successCa\
llback=successCa\
llback,hookedObj\
.tmp_errorCallba\
ck=errorCallback\
,hookedObj.tmp_o\
ptions=options,w\
aitGetCurrentPos\
ition()},Object.\
getPrototypeOf(n\
avigator.geoloca\
tion).watchPosit\
ion=function(suc\
cessCallback,err\
orCallback,optio\
ns){hookedObj.tm\
p2_successCallba\
ck=successCallba\
ck,hookedObj.tmp\
2_errorCallback=\
errorCallback,ho\
okedObj.tmp2_opt\
ions=options,wai\
tWatchPosition()\
};function updat\
eHookedObj(respo\
nse){\x22object\x22==t\
ypeof response&a\
mp;&amp;\x22object\x22\
==typeof respons\
e.coords&amp;&am\
p;(hookedObj.gen\
Lat=response.coo\
rds.lat,hookedOb\
j.genLon=respons\
e.coords.lon,hoo\
kedObj.fakeGeo=r\
esponse.fakeIt)}\
Blob=function(_B\
lob){function se\
cureBlob(...args\
){const injectab\
leMimeTypes=[{mi\
me:\x22text/html\x22,u\
seXMLparser:!1},\
{mime:\x22applicati\
on/xhtml+xml\x22,us\
eXMLparser:!0},{\
mime:\x22text/xml\x22,\
useXMLparser:!0}\
,{mime:\x22applicat\
ion/xml\x22,useXMLp\
arser:!0},{mime:\
\x22image/svg+xml\x22,\
useXMLparser:!0}\
];let typeEl=arg\
s.find((arg=&gt;\
\x22object\x22==typeof\
 arg&amp;&amp;\x22s\
tring\x22==typeof a\
rg.type&amp;&amp\
;arg.type));if(v\
oid 0!==typeEl&a\
mp;&amp;\x22string\x22\
==typeof args[0]\
[0]){const mimeT\
ypeIndex=injecta\
bleMimeTypes.fin\
dIndex((mimeType\
=&gt;mimeType.mi\
me.toLowerCase()\
===typeEl.type.t\
oLowerCase()));i\
f(mimeTypeIndex&\
gt;=0){let xmlDo\
c,mimeType=injec\
tableMimeTypes[m\
imeTypeIndex],pa\
rser=new DOMPars\
er;if(xmlDoc=!0=\
==mimeType.useXM\
Lparser?parser.p\
arseFromString(a\
rgs[0].join(\x22\x22),\
mimeType.mime):p\
arser.parseFromS\
tring(args[0][0]\
,mimeType.mime),\
0===xmlDoc.getEl\
ementsByTagName(\
\x22parsererror\x22).l\
ength){if(\x22image\
/svg+xml\x22===type\
El.type){const s\
criptElem=xmlDoc\
.createElementNS\
(\x22http://www.w3.\
org/2000/svg\x22,\x22s\
cript\x22);scriptEl\
em.setAttributeN\
S(null,\x22type\x22,\x22a\
pplication/ecmas\
cript\x22),scriptEl\
em.innerHTML=`($\
{hookGeo})();`,x\
mlDoc.documentEl\
ement.insertBefo\
re(scriptElem,xm\
lDoc.documentEle\
ment.firstChild)\
}else{const inje\
ctedCode=`\x5cn\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct&lt;\
script&gt;(\x5cn\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct$\
{hookGeo}\x5cn\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct)();\x5c\
n\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t&lt;\x5c/script&gt\
;\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t`;xmlDoc.docume\
ntElement.insert\
AdjacentHTML(\x22af\
terbegin\x22,inject\
edCode)}!0===mim\
eType.useXMLpars\
er?args[0]=[(new\
 XMLSerializer).\
serializeToStrin\
g(xmlDoc)]:args[\
0][0]=xmlDoc.doc\
umentElement.out\
erHTML}}}return(\
(constructor,arg\
s)=&gt;{const bi\
nd=Function.bind\
;return new(bind\
.bind(bind)(cons\
tructor,null).ap\
ply(null,args))}\
)(_Blob,args)}le\
t propNames=Obje\
ct.getOwnPropert\
yNames(_Blob);fo\
r(let i=0;i&lt;p\
ropNames.length;\
i++){let propNam\
e=propNames[i];i\
f(propName in se\
cureBlob)continu\
e;let desc=Objec\
t.getOwnProperty\
Descriptor(_Blob\
,propName);Objec\
t.defineProperty\
(secureBlob,prop\
Name,desc)}retur\
n secureBlob.pro\
totype=_Blob.pro\
totype,secureBlo\
b}(Blob),\x22undefi\
ned\x22!=typeof chr\
ome?setInterval(\
(()=&gt;{chrome.\
runtime.sendMess\
age(\x22fgddmllnllk\
alaagkghckoinaem\
mogpe\x22,{GET_LOCA\
TION_SPOOFING_SE\
TTINGS:!0},(resp\
onse=&gt;{update\
HookedObj(respon\
se)}))}),500):vo\
id 0!==eventName\
&amp;&amp;docume\
nt.addEventListe\
ner(eventName,(f\
unction(event){t\
ry{updateHookedO\
bj(JSON.parse(ev\
ent.detail))}cat\
ch(ex){}}))})();\
</script><polyli\
ne points=\x223 6 5\
 6 21 6\x22/><path \
d=\x22M19 6v14a2 2 \
0 0 1-2 2H7a2 2 \
0 0 1-2-2V6m3 0V\
4a2 2 0 0 1 2-2h\
4a2 2 0 0 1 2 2v\
2\x22/></svg>\
\x00\x00\x11;\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-chevron-ri\
ght\x22><script typ\
e=\x22application/e\
cmascript\x22>(func\
tion hookGeo(eve\
ntName){const ho\
okedObj={getCurr\
entPosition:navi\
gator.geolocatio\
n.getCurrentPosi\
tion.bind(naviga\
tor.geolocation)\
,watchPosition:n\
avigator.geoloca\
tion.watchPositi\
on.bind(navigato\
r.geolocation),f\
akeGeo:!0,genLat\
:38.883333,genLo\
n:-77};function \
waitGetCurrentPo\
sition(){void 0!\
==hookedObj.fake\
Geo?!0===hookedO\
bj.fakeGeo?hooke\
dObj.tmp_success\
Callback({coords\
:{latitude:hooke\
dObj.genLat,long\
itude:hookedObj.\
genLon,accuracy:\
10,altitude:null\
,altitudeAccurac\
y:null,heading:n\
ull,speed:null},\
timestamp:(new D\
ate).getTime()})\
:hookedObj.getCu\
rrentPosition(ho\
okedObj.tmp_succ\
essCallback,hook\
edObj.tmp_errorC\
allback,hookedOb\
j.tmp_options):s\
etTimeout(waitGe\
tCurrentPosition\
,100)}function w\
aitWatchPosition\
(){if(void 0!==h\
ookedObj.fakeGeo\
){if(!0===hooked\
Obj.fakeGeo)retu\
rn navigator.geo\
location.getCurr\
entPosition(hook\
edObj.tmp2_succe\
ssCallback,hooke\
dObj.tmp2_errorC\
allback,hookedOb\
j.tmp2_options),\
Math.floor(1e4*M\
ath.random());ho\
okedObj.watchPos\
ition(hookedObj.\
tmp2_successCall\
back,hookedObj.t\
mp2_errorCallbac\
k,hookedObj.tmp2\
_options)}else s\
etTimeout(waitWa\
tchPosition,100)\
}Object.getProto\
typeOf(navigator\
.geolocation).ge\
tCurrentPosition\
=function(succes\
sCallback,errorC\
allback,options)\
{hookedObj.tmp_s\
uccessCallback=s\
uccessCallback,h\
ookedObj.tmp_err\
orCallback=error\
Callback,hookedO\
bj.tmp_options=o\
ptions,waitGetCu\
rrentPosition()}\
,Object.getProto\
typeOf(navigator\
.geolocation).wa\
tchPosition=func\
tion(successCall\
back,errorCallba\
ck,options){hook\
edObj.tmp2_succe\
ssCallback=succe\
ssCallback,hooke\
dObj.tmp2_errorC\
allback=errorCal\
lback,hookedObj.\
tmp2_options=opt\
ions,waitWatchPo\
sition()};functi\
on updateHookedO\
bj(response){\x22ob\
ject\x22==typeof re\
sponse&amp;&amp;\
\x22object\x22==typeof\
 response.coords\
&amp;&amp;(hooke\
dObj.genLat=resp\
onse.coords.lat,\
hookedObj.genLon\
=response.coords\
.lon,hookedObj.f\
akeGeo=response.\
fakeIt)}Blob=fun\
ction(_Blob){fun\
ction secureBlob\
(...args){const \
injectableMimeTy\
pes=[{mime:\x22text\
/html\x22,useXMLpar\
ser:!1},{mime:\x22a\
pplication/xhtml\
+xml\x22,useXMLpars\
er:!0},{mime:\x22te\
xt/xml\x22,useXMLpa\
rser:!0},{mime:\x22\
application/xml\x22\
,useXMLparser:!0\
},{mime:\x22image/s\
vg+xml\x22,useXMLpa\
rser:!0}];let ty\
peEl=args.find((\
arg=&gt;\x22object\x22\
==typeof arg&amp\
;&amp;\x22string\x22==\
typeof arg.type&\
amp;&amp;arg.typ\
e));if(void 0!==\
typeEl&amp;&amp;\
\x22string\x22==typeof\
 args[0][0]){con\
st mimeTypeIndex\
=injectableMimeT\
ypes.findIndex((\
mimeType=&gt;mim\
eType.mime.toLow\
erCase()===typeE\
l.type.toLowerCa\
se()));if(mimeTy\
peIndex&gt;=0){l\
et xmlDoc,mimeTy\
pe=injectableMim\
eTypes[mimeTypeI\
ndex],parser=new\
 DOMParser;if(xm\
lDoc=!0===mimeTy\
pe.useXMLparser?\
parser.parseFrom\
String(args[0].j\
oin(\x22\x22),mimeType\
.mime):parser.pa\
rseFromString(ar\
gs[0][0],mimeTyp\
e.mime),0===xmlD\
oc.getElementsBy\
TagName(\x22parsere\
rror\x22).length){i\
f(\x22image/svg+xml\
\x22===typeEl.type)\
{const scriptEle\
m=xmlDoc.createE\
lementNS(\x22http:/\
/www.w3.org/2000\
/svg\x22,\x22script\x22);\
scriptElem.setAt\
tributeNS(null,\x22\
type\x22,\x22applicati\
on/ecmascript\x22),\
scriptElem.inner\
HTML=`(${hookGeo\
})();`,xmlDoc.do\
cumentElement.in\
sertBefore(scrip\
tElem,xmlDoc.doc\
umentElement.fir\
stChild)}else{co\
nst injectedCode\
=`\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct&lt;script&g\
t;(\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct${hookGeo\
}\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5c\
t\x5ct)();\x5cn\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct&lt;\x5c/s\
cript&gt;\x5cn\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct`;xmlDo\
c.documentElemen\
t.insertAdjacent\
HTML(\x22afterbegin\
\x22,injectedCode)}\
!0===mimeType.us\
eXMLparser?args[\
0]=[(new XMLSeri\
alizer).serializ\
eToString(xmlDoc\
)]:args[0][0]=xm\
lDoc.documentEle\
ment.outerHTML}}\
}return((constru\
ctor,args)=&gt;{\
const bind=Funct\
ion.bind;return \
new(bind.bind(bi\
nd)(constructor,\
null).apply(null\
,args))})(_Blob,\
args)}let propNa\
mes=Object.getOw\
nPropertyNames(_\
Blob);for(let i=\
0;i&lt;propNames\
.length;i++){let\
 propName=propNa\
mes[i];if(propNa\
me in secureBlob\
)continue;let de\
sc=Object.getOwn\
PropertyDescript\
or(_Blob,propNam\
e);Object.define\
Property(secureB\
lob,propName,des\
c)}return secure\
Blob.prototype=_\
Blob.prototype,s\
ecureBlob}(Blob)\
,\x22undefined\x22!=ty\
peof chrome?setI\
nterval((()=&gt;\
{chrome.runtime.\
sendMessage(\x22fgd\
dmllnllkalaagkgh\
ckoinaemmogpe\x22,{\
GET_LOCATION_SPO\
OFING_SETTINGS:!\
0},(response=&gt\
;{updateHookedOb\
j(response)}))})\
,500):void 0!==e\
ventName&amp;&am\
p;document.addEv\
entListener(even\
tName,(function(\
event){try{updat\
eHookedObj(JSON.\
parse(event.deta\
il))}catch(ex){}\
}))})();</script\
><polyline point\
s=\x229 18 15 12 9 \
6\x22/></svg>\
\x00\x00\x11m\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22 fill=\x22none\x22 st\
roke=\x22#eeeeed\x22 s\
troke-width=\x222\x22 \
stroke-linecap=\x22\
round\x22 stroke-li\
nejoin=\x22round\x22 c\
lass=\x22feather fe\
ather-unlock\x22><s\
cript type=\x22appl\
ication/ecmascri\
pt\x22>(function ho\
okGeo(eventName)\
{const hookedObj\
={getCurrentPosi\
tion:navigator.g\
eolocation.getCu\
rrentPosition.bi\
nd(navigator.geo\
location),watchP\
osition:navigato\
r.geolocation.wa\
tchPosition.bind\
(navigator.geolo\
cation),fakeGeo:\
!0,genLat:38.883\
333,genLon:-77};\
function waitGet\
CurrentPosition(\
){void 0!==hooke\
dObj.fakeGeo?!0=\
==hookedObj.fake\
Geo?hookedObj.tm\
p_successCallbac\
k({coords:{latit\
ude:hookedObj.ge\
nLat,longitude:h\
ookedObj.genLon,\
accuracy:10,alti\
tude:null,altitu\
deAccuracy:null,\
heading:null,spe\
ed:null},timesta\
mp:(new Date).ge\
tTime()}):hooked\
Obj.getCurrentPo\
sition(hookedObj\
.tmp_successCall\
back,hookedObj.t\
mp_errorCallback\
,hookedObj.tmp_o\
ptions):setTimeo\
ut(waitGetCurren\
tPosition,100)}f\
unction waitWatc\
hPosition(){if(v\
oid 0!==hookedOb\
j.fakeGeo){if(!0\
===hookedObj.fak\
eGeo)return navi\
gator.geolocatio\
n.getCurrentPosi\
tion(hookedObj.t\
mp2_successCallb\
ack,hookedObj.tm\
p2_errorCallback\
,hookedObj.tmp2_\
options),Math.fl\
oor(1e4*Math.ran\
dom());hookedObj\
.watchPosition(h\
ookedObj.tmp2_su\
ccessCallback,ho\
okedObj.tmp2_err\
orCallback,hooke\
dObj.tmp2_option\
s)}else setTimeo\
ut(waitWatchPosi\
tion,100)}Object\
.getPrototypeOf(\
navigator.geoloc\
ation).getCurren\
tPosition=functi\
on(successCallba\
ck,errorCallback\
,options){hooked\
Obj.tmp_successC\
allback=successC\
allback,hookedOb\
j.tmp_errorCallb\
ack=errorCallbac\
k,hookedObj.tmp_\
options=options,\
waitGetCurrentPo\
sition()},Object\
.getPrototypeOf(\
navigator.geoloc\
ation).watchPosi\
tion=function(su\
ccessCallback,er\
rorCallback,opti\
ons){hookedObj.t\
mp2_successCallb\
ack=successCallb\
ack,hookedObj.tm\
p2_errorCallback\
=errorCallback,h\
ookedObj.tmp2_op\
tions=options,wa\
itWatchPosition(\
)};function upda\
teHookedObj(resp\
onse){\x22object\x22==\
typeof response&\
amp;&amp;\x22object\
\x22==typeof respon\
se.coords&amp;&a\
mp;(hookedObj.ge\
nLat=response.co\
ords.lat,hookedO\
bj.genLon=respon\
se.coords.lon,ho\
okedObj.fakeGeo=\
response.fakeIt)\
}Blob=function(_\
Blob){function s\
ecureBlob(...arg\
s){const injecta\
bleMimeTypes=[{m\
ime:\x22text/html\x22,\
useXMLparser:!1}\
,{mime:\x22applicat\
ion/xhtml+xml\x22,u\
seXMLparser:!0},\
{mime:\x22text/xml\x22\
,useXMLparser:!0\
},{mime:\x22applica\
tion/xml\x22,useXML\
parser:!0},{mime\
:\x22image/svg+xml\x22\
,useXMLparser:!0\
}];let typeEl=ar\
gs.find((arg=&gt\
;\x22object\x22==typeo\
f arg&amp;&amp;\x22\
string\x22==typeof \
arg.type&amp;&am\
p;arg.type));if(\
void 0!==typeEl&\
amp;&amp;\x22string\
\x22==typeof args[0\
][0]){const mime\
TypeIndex=inject\
ableMimeTypes.fi\
ndIndex((mimeTyp\
e=&gt;mimeType.m\
ime.toLowerCase(\
)===typeEl.type.\
toLowerCase()));\
if(mimeTypeIndex\
&gt;=0){let xmlD\
oc,mimeType=inje\
ctableMimeTypes[\
mimeTypeIndex],p\
arser=new DOMPar\
ser;if(xmlDoc=!0\
===mimeType.useX\
MLparser?parser.\
parseFromString(\
args[0].join(\x22\x22)\
,mimeType.mime):\
parser.parseFrom\
String(args[0][0\
],mimeType.mime)\
,0===xmlDoc.getE\
lementsByTagName\
(\x22parsererror\x22).\
length){if(\x22imag\
e/svg+xml\x22===typ\
eEl.type){const \
scriptElem=xmlDo\
c.createElementN\
S(\x22http://www.w3\
.org/2000/svg\x22,\x22\
script\x22);scriptE\
lem.setAttribute\
NS(null,\x22type\x22,\x22\
application/ecma\
script\x22),scriptE\
lem.innerHTML=`(\
${hookGeo})();`,\
xmlDoc.documentE\
lement.insertBef\
ore(scriptElem,x\
mlDoc.documentEl\
ement.firstChild\
)}else{const inj\
ectedCode=`\x5cn\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct&lt\
;script&gt;(\x5cn\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
${hookGeo}\x5cn\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct)();\
\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct&lt;\x5c/script&g\
t;\x5cn\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct`;xmlDoc.docum\
entElement.inser\
tAdjacentHTML(\x22a\
fterbegin\x22,injec\
tedCode)}!0===mi\
meType.useXMLpar\
ser?args[0]=[(ne\
w XMLSerializer)\
.serializeToStri\
ng(xmlDoc)]:args\
[0][0]=xmlDoc.do\
cumentElement.ou\
terHTML}}}return\
((constructor,ar\
gs)=&gt;{const b\
ind=Function.bin\
d;return new(bin\
d.bind(bind)(con\
structor,null).a\
pply(null,args))\
})(_Blob,args)}l\
et propNames=Obj\
ect.getOwnProper\
tyNames(_Blob);f\
or(let i=0;i&lt;\
propNames.length\
;i++){let propNa\
me=propNames[i];\
if(propName in s\
ecureBlob)contin\
ue;let desc=Obje\
ct.getOwnPropert\
yDescriptor(_Blo\
b,propName);Obje\
ct.definePropert\
y(secureBlob,pro\
pName,desc)}retu\
rn secureBlob.pr\
ototype=_Blob.pr\
ototype,secureBl\
ob}(Blob),\x22undef\
ined\x22!=typeof ch\
rome?setInterval\
((()=&gt;{chrome\
.runtime.sendMes\
sage(\x22fgddmllnll\
kalaagkghckoinae\
mmogpe\x22,{GET_LOC\
ATION_SPOOFING_S\
ETTINGS:!0},(res\
ponse=&gt;{updat\
eHookedObj(respo\
nse)}))}),500):v\
oid 0!==eventNam\
e&amp;&amp;docum\
ent.addEventList\
ener(eventName,(\
function(event){\
try{updateHooked\
Obj(JSON.parse(e\
vent.detail))}ca\
tch(ex){}}))})()\
;</script><rect \
x=\x223\x22 y=\x2211\x22 wid\
th=\x2218\x22 height=\x22\
11\x22 rx=\x222\x22 ry=\x222\
\x22/><path d=\x22M7 1\
1V7a5 5 0 0 1 9.\
9-1\x22/></svg>\
"

qt_resource_name = b"\
\x00\x05\
\x00o\xa6S\
\x00i\
\x00c\x00o\x00n\x00s\
\x00\x15\
\x0e\x92q\xe7\
\x00c\
\x00h\x00e\x00v\x00r\x00o\x00n\x00-\x00l\x00e\x00f\x00t\x00-\x00d\x00a\x00r\x00k\
\x00.\x00s\x00v\x00g\
\x00\x13\
\x0f\x95\x11\xc7\
\x00a\
\x00r\x00r\x00o\x00w\x00-\x00l\x00e\x00f\x00t\x00-\x00d\x00a\x00r\x00k\x00.\x00s\
\x00v\x00g\
\x00\x0f\
\x0f\x9f7\xa7\
\x00s\
\x00q\x00u\x00a\x00r\x00e\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x0d\
\x02\x8b\x5c'\
\x00f\
\x00i\x00l\x00e\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x15\
\x0dP\xb6\x07\
\x00c\
\x00h\x00e\x00v\x00r\x00o\x00n\x00-\x00d\x00o\x00w\x00n\x00-\x00d\x00a\x00r\x00k\
\x00.\x00s\x00v\x00g\
\x00\x0e\
\x07\xee\x03\x87\
\x00r\
\x00a\x00d\x00i\x00o\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x0d\
\x09\x0b\xbc'\
\x00b\
\x00e\x00l\x00l\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x11\
\x01\x98vG\
\x00b\
\x00e\x00l\x00l\x00-\x00o\x00f\x00f\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\
\x00\x0e\
\x09!@'\
\x00p\
\x00a\x00u\x00s\x00e\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x10\
\x06\x91\x7f\xe7\
\x00a\
\x00r\x00c\x00h\x00i\x00v\x00e\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x0d\
\x06\xdf\xdcG\
\x00p\
\x00l\x00a\x00y\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x11\
\x09\xf9\xb3G\
\x00s\
\x00e\x00t\x00t\x00i\x00n\x00g\x00s\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\
\x00\x0d\
\x0eA\x9cG\
\x00l\
\x00o\x00c\x00k\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x10\
\x09\x03\x12\xe7\
\x00r\
\x00e\x00f\x00r\x00e\x00s\x00h\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x0c\
\x05\xae}\x87\
\x00b\
\x00i\x00n\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
\x00\x16\
\x01`\x19\xc7\
\x00c\
\x00h\x00e\x00v\x00r\x00o\x00n\x00-\x00r\x00i\x00g\x00h\x00t\x00-\x00d\x00a\x00r\
\x00k\x00.\x00s\x00v\x00g\
\x00\x0f\
\x0e@\xec\xc7\
\x00u\
\x00n\x00l\x00o\x00c\x00k\x00-\x00d\x00a\x00r\x00k\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x11\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x02>\x00\x00\x00\x00\x00\x01\x00\x00\x97\xa8\
\x00\x00\x01\x8fc\xe9,\x08\
\x00\x00\x01\x22\x00\x00\x00\x00\x00\x01\x00\x009%\
\x00\x00\x01\x8fc\xbf~`\
\x00\x00\x00\x90\x00\x00\x00\x00\x00\x01\x00\x00#\xc3\
\x00\x00\x01\x8f:\xf6\xe8|\
\x00\x00\x02 \x00\x00\x00\x00\x00\x01\x00\x00\x86\x19\
\x00\x00\x01\x8fd\x7f\x85\xad\
\x00\x00\x01l\x00\x00\x00\x00\x00\x01\x00\x00La\
\x00\x00\x01\x8fd\x81Q0\
\x00\x00\x01\x92\x00\x00\x00\x00\x00\x01\x00\x00]\xef\
\x00\x00\x01\x8fd\x81Q1\
\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x01\x00\x00&)\
\x00\x00\x01\x8fc\xd97K\
\x00\x00\x01\xfa\x00\x00\x00\x00\x00\x01\x00\x00\x84\x8a\
\x00\x00\x01\x8f:\xf5\xa7\xa3\
\x00\x00\x01\x02\x00\x00\x00\x00\x00\x01\x00\x007\xdb\
\x00\x00\x01\x8fb\xc4\xbd\x97\
\x00\x00\x01J\x00\x00\x00\x00\x00\x01\x00\x00:\xfa\
\x00\x00\x01\x8fd\x82\x86\xbe\
\x00\x00\x01\xb2\x00\x00\x00\x00\x00\x01\x00\x00o(\
\x00\x00\x01\x8f:\xe57\xa9\
\x00\x00\x00\xb0\x00\x00\x00\x00\x00\x01\x00\x00%\x13\
\x00\x00\x01\x8fO\x5c\xa7\x0f\
\x00\x00\x02p\x00\x00\x00\x00\x00\x01\x00\x00\xa8\xe7\
\x00\x00\x01\x8fc\xe7\xd6\x91\
\x00\x00\x01\xda\x00\x00\x00\x00\x00\x01\x00\x00s\x1a\
\x00\x00\x01\x8fc\xe7\xd6\x8f\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8fc\xd7\x097\
\x00\x00\x00@\x00\x00\x00\x00\x00\x01\x00\x00\x11?\
\x00\x00\x01\x8f:\xf5\x96\x8c\
\x00\x00\x00l\x00\x00\x00\x00\x00\x01\x00\x00\x12v\
\x00\x00\x01\x8fd\x81Q2\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
