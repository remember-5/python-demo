webpackJsonp([84],{SdNZ:function(e,r){},Xb9r:function(e,r,t){"use strict";Object.defineProperty(r,"__esModule",{value:!0});var n=t("wggp"),a=t.n(n),i=t("PbuP"),o=t("yTDo"),s=t("R9IU"),u=t("jIOT"),l=t("YjV0"),c=t("VKKs"),p=(t("PvbX"),function(){return function(e,r){if(Array.isArray(e))return e;if(Symbol.iterator in Object(e))return function(e,r){var t=[],n=!0,a=!1,i=void 0;try{for(var o,s=e[Symbol.iterator]();!(n=(o=s.next()).done)&&(t.push(o.value),!r||t.length!==r);n=!0);}catch(e){a=!0,i=e}finally{try{!n&&s.return&&s.return()}finally{if(a)throw i}}return t}(e,r);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}());function f(e){if(Array.isArray(e)){for(var r=0,t=Array(e.length);r<e.length;r++)t[r]=e[r];return t}return Array.from(e)}function d(e){return function(){var r=e.apply(this,arguments);return new Promise(function(e,t){return function n(a,i){try{var o=r[a](i),s=o.value}catch(e){return void t(e)}if(!o.done)return Promise.resolve(s).then(function(e){n("next",e)},function(e){n("throw",e)});e(s)}("next")})}}var g={inject:["farmDetailRefs"],data:function(){return{gismap:null,gisloading:!0,temptoken:"",tileMap:{weixing:"/shanghaiArcGIS/rest/services/SHMAP_IMAGE/MapServer"},options:{url:"http://gov.snkoudai.com/mapdemo/arcgis3.28/init.js"},allPlotMarkerLayer:null,allPlotPolygonLayer:null,activePlotsLayer:null,greenCertPlotsLayer:null,greenCertPlotsIsActive:!1,serviceMap:{nongyongdi:"",dapeng:"",hezuosheNaturalBorder:""},homeLatLng:[121.12961431068945,30.979833911253177,121.69403691811132,31.266851733518802],wxLayerUpdateEnd:!1,plotidMapImg:{},tipsShow:!1}},props:{landList:{default:function(){return[]},type:Array},cropList:{default:function(){return[]},type:Array}},computed:{landGisIds:function(){return this.landList.map(function(e){return e.gisPlotId})}},mounted:function(){var e=this;return d(regeneratorRuntime.mark(function r(){return regeneratorRuntime.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:return r.next=2,e.initMap();case 2:case"end":return r.stop()}},r,e)}))()},methods:{initFeature:function(){var e=this,r=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return d(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:if(!e.landList.length){t.next=5;break}return t.next=3,e.renderPlotToMap(e.landList,r);case 3:t.sent.forEach(function(r,t){var n=r.attributes.DPDKID||r.attributes.DKID;e.landList.forEach(function(e){e.gisPlotId===n&&(e.hasArea=!0)})});case 5:case"end":return t.stop()}},t,e)}))()},initMap:function(){var e,r=this;return new Promise((e=d(regeneratorRuntime.mark(function e(t){var n,a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return n=Object(c.b)("govGovernmentSubjectVO"),a="310100",n&&n.cityId&&2===n.subjectLevel&&(a=n.cityId),n&&n.countyId&&3===n.subjectLevel&&(a=n.countyId),a=i.a.hasOwnProperty(a)?a:"310100",r.serviceMap.nongyongdi=i.a[a].nongyongdi,r.serviceMap.dapeng=i.a[a].dapeng,r.serviceMap.hezuosheNaturalBorder=i.a[a].hezuosheNaturalBorder,r.homeLatLng=i.a[a].centerExtend,e.next=11,Object(o.a)(r);case 11:r.temptoken=e.sent,r.$nextTick(d(regeneratorRuntime.mark(function e(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,r.renderMap();case 2:return e.next=4,r.listenrMapInitStatus();case 4:if(e.sent){e.next=8;break}return window.location.reload(),e.abrupt("return");case 8:dojo.connect(r.gismap,"onClick",r.searchPointer),t();case 10:case"end":return e.stop()}},e,r)})));case 13:case"end":return e.stop()}},e,r)})),function(r){return e.apply(this,arguments)}))},renderMap:function(){var e=this;return new Promise(function(r){a.a.loadModules(["esri/map","esri/layers/ArcGISTiledMapServiceLayer","esri/layers/ArcGISDynamicMapServiceLayer","esri/layers/ImageParameters","esri/geometry/Point","esri/SpatialReference","esri/geometry/Extent","esri/layers/GraphicsLayer"],e.options).then(function(t){var n=p(t,8),a=n[0],i=n[1],o=(n[2],n[3],n[4],n[5],n[6]),s=n[7],u=e,l=new a("gismap",{extent:new(Function.prototype.bind.apply(o,[null].concat(f(e.homeLatLng),[new esri.SpatialReference({wkid:4326})]))),logo:!1,optimizePanAnimation:!0});dojo.connect(l,"onExtentChange",function(){}),dojo.connect(l,"onZoomEnd",function(e){var r=l.getZoom();u.updateMarker(u.allPlotMarkerLayer.graphics,r+10)});var c=new i(e.tileMap.weixing,{id:"weixing_ditu"});c.on("update-end",function(e){console.log(e.error),u.wxLayerUpdateEnd=!0});try{l.addLayer(c)}catch(e){console.log(e),console.log("报错")}e.allPlotPolygonLayer=new s({visible:!0}),l.addLayer(e.allPlotPolygonLayer),e.greenCertPlotsLayer=new s({visible:!0}),l.addLayer(e.greenCertPlotsLayer),e.activePlotsLayer=new s({visible:!0}),l.addLayer(e.activePlotsLayer),e.allPlotMarkerLayer=new s({visible:!0}),l.addLayer(e.allPlotMarkerLayer),e.gismap=l,r(!0)},function(e){r(!1)})})},listenrMapInitStatus:function(){var e,r=this,t=this,n=!1,a=t.$route.path;function i(){var e,r=this;return new Promise((e=d(regeneratorRuntime.mark(function e(i){var o;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:o=function(){if(t.$route.path===a&&!n){var e=document.getElementById("gismap_weixing_ditu");e&&""!==e.innerHTML&&(n=!0,i(!0))}},setTimeout(o,200),setTimeout(o,500),setTimeout(o,1e3),setTimeout(o,2e3),setTimeout(o,4e3),setTimeout(o,5e3),setTimeout(function(){if(t.$route.path===a&&!n){var e=document.getElementById("gismap_weixing_ditu");e&&""!==e.innerHTML?(n=!0,i(!0)):(document.getElementById("gismap").innerHTML="",console.log("天地图加载有问题 重新加载"),i(!1))}},7e3);case 8:case"end":return e.stop()}},e,r)})),function(r){return e.apply(this,arguments)}))}return new Promise((e=d(regeneratorRuntime.mark(function e(t){var n;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,i();case 2:n=e.sent,t(n);case 4:case"end":return e.stop()}},e,r)})),function(r){return e.apply(this,arguments)}))},initServerLayer:function(){var e=this,r=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"nongyongdi";return new Promise(function(t){var n=e.serviceMap[r]+"?token="+e.temptoken;a.a.loadModules(["esri/layers/ArcGISDynamicMapServiceLayer"],e.options).then(function(e){p(e,1)[0];var a=new esri.layers.ArcGISDynamicMapServiceLayer(n,{id:r,outFields:["*"]});t(a)},function(e){t(!1)})})},renderAllPolygon:function(e,r){var t,n=this,a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:1;return new Promise((t=d(regeneratorRuntime.mark(function t(i){var o,s,u,l,c;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:if(e.length){t.next=3;break}return i(),t.abrupt("return");case 3:return t.next=5,n.mergePolygonRander(e,a);case 5:o=t.sent,s=p(o,2),u=s[0],l=s[1],u.map(function(e){r.add(e)}),c={},l.map(function(e){c[e.plotid]=e}),r.plotFeatures=Object.assign({},c),i();case 14:case"end":return t.stop()}},t,n)})),function(e){return t.apply(this,arguments)}))},mergePolygonRander:function(e,r){var t=this;return new Promise(function(n){a.a.loadModules(["esri/graphic","esri/geometry/Polygon","esri/SpatialReference","esri/symbols/SimpleFillSymbol","esri/symbols/SimpleLineSymbol"],t.options).then(function(a){var i=p(a,5),o=i[0],s=i[1],u=i[2],l=i[3],c=i[4];if(0!==e.length){for(var d={},g=[],m=1===r?4:1,h=0;h<e.length;h++){var y=t.getNowAreaColor(e[h],r),v=p(y,2),w=v[0],P=v[1],b=JSON.parse(JSON.stringify(e[h].geometry.rings)),S=(w+P+m).split(",").join(""),L=e[h].attributes.DPDKID||e[h].attributes.DKID;if(g.push({plotid:L,plotplusid:t.getNYDid(L),areaColor:w,borderColor:P,borderwidth:m,rings:b}),d[S]){b=JSON.parse(JSON.stringify(e[h].geometry.rings));d[S].rings=d[S].rings.concat(b)}else d[S]={areaColor:w,borderColor:P,borderwidth:m,rings:b}}var x=[];for(var k in d){for(var I=d[k],M=(w=I.areaColor,P=I.borderColor,m=I.borderwidth,b=I.rings,new l(l.STYLE_SOLID,new c(c.STYLE_SOLID,new dojo.Color(P),m),new dojo.Color([].concat(f(w),[.3])))),D=new s(new u({wkid:4326})),A=0,C=b.length;A<C;A++)D.addRing(b[A]);x.push(new o(D,M))}n([x,g])}else n(!1)})})},updateFeature:function(e,r,t){var n=this,i=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{};return new Promise(function(o){a.a.loadModules(["esri/graphic","esri/geometry/Polygon","esri/SpatialReference","esri/symbols/SimpleFillSymbol","esri/symbols/SimpleLineSymbol"],n.options).then(function(a){var s=p(a,5),u=s[0],l=s[1],c=s[2],d=s[3],g=s[4];if(!e.length)return t.clear(),void o(!0);var m=!1,h={},y=new l(new c({wkid:4326}));if(e.map(function(e){if(r.hasOwnProperty(e)){m=!0;var t=n.getNowAreaColor(r[e],2),a=p(t,2),o=a[0],s=a[1],u=i.stroke,l=void 0===u?s:u,c=i.fillOpacity,f=void 0===c?.3:c,d=i.fill,g=void 0===d?o:d,y=JSON.parse(JSON.stringify(r[e].rings)),v=(g+l+f).split(",").join("");if(h[v]){y=JSON.parse(JSON.stringify(r[e].rings));h[v].rings=h[v].rings.concat(y)}else h[v]={areaColor:g,borderColor:l,borderwidth:4,fillOpacity:f,rings:y}}}),m)for(var v in h){for(var w=h[v],P=w.areaColor,b=w.borderColor,S=w.borderwidth,L=w.fillOpacity,x=w.rings,k=new d(d.STYLE_SOLID,new g(g.STYLE_SOLID,new dojo.Color(b),S),new dojo.Color([].concat(f(P),[L]))),I=(y=new l(new c({wkid:4326})),0),M=x.length;I<M;I++)y.addRing(x[I]);t.add(new u(y,k))}o(m)})})},renderAllMarker:function(e,r){var t=this,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:17,i=this;return new Promise(function(o){0!==e.length?a.a.loadModules(["esri/graphic","esri/geometry/Point","esri/symbols/PictureMarkerSymbol","esri/SpatialReference"],t.options).then(function(t){for(var a=p(t,4),u=a[0],l=a[1],c=a[2],f=a[3],d=0;d<e.length;d++){var g=JSON.parse(JSON.stringify(e[d].geometry.rings)),m=e[d].attributes.DPDKID||e[d].attributes.DKID;h(g,i.aliimgCircle(i.plotidMapImg[m],48),r)}function h(e,r,t){var a=[];e[0].map(function(e){2===e.length&&a.push(e)});var o=[];a.map(function(e){2===e.length&&o.push(s.point(e))});var d=s.featureCollection(o),g=s.center(d),m=i.computeMarkerPosAnchor(n),h=p(m,2),y=h[0],v=h[1],w=new l(g.geometry.coordinates,new f({wkid:4326})),P=new c({url:r,width:y[0],height:y[1],xoffset:v[0],yoffset:v[1]});t.add(new u(w,P))}o()}):o()})},updateMarker:function(){var e=this,r=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments[1];r.map(function(r){var n=r.symbol,a=e.computeMarkerPosAnchor(t),i=p(a,2),o=i[0],s=i[1];n.setWidth(o[0]),n.setHeight(o[1]),n.setOffset.apply(n,f(s))})},computeMarkerPosAnchor:function(e){var r=arguments.length>1&&void 0!==arguments[1]?arguments[1]:1,t=arguments.length>2&&void 0!==arguments[2]?arguments[2]:0,n=arguments.length>3&&void 0!==arguments[3]&&arguments[3]?{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:2,9:4,10:4,11:4,12:6,13:6,14:6,15:6,16:8,17:8,18:12,19:18,20:36,21:42,22:48}[e]:{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:2,9:4,10:4,11:4,12:6,13:8,14:8,15:8,16:12,17:16,18:24,19:32,20:40,21:48,22:56}[e],a=[[],[[0,0]],[[24,12],[0,12]],[[12,24],[0,0],[24,0]],[[24,24],[0,24],[0,0],[24,0]]].map(function(e){return e.map(function(e){return e[0]=parseInt(e[0]*n/24),e[1]=parseInt(e[1]*n/24),e}),e})[r][t];return[[n,n],a]},aliimgCircle:function(e,r){return r=r||100,e&&-1!==e.indexOf(".aliyuncs.com/")?e+"?x-oss-process=image/resize,w_"+r+",h_"+r+",m_fill/auto-orient,1/quality,q_100/sharpen,80/format,png":e},getCenterAZoom:function(e){var r=this,t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"company";return new Promise(function(n){for(var i=[],o=[],s=[],u=[],l=0;l<e.length;l++){var c=e[l].geometry.getExtent();i.push(c.xmin),o.push(c.ymin),s.push(c.xmax),u.push(c.ymax)}var d=function(e,r){if(4!==e.length)return[];var t=e[2]-e[0],n=e[3]-e[1];e[0],e[1];if("company"===r){var a=.25*t,i=.25*n;return[e[0]-5*a,e[1]-i,e[2]+5*a,e[3]+1.5*i]}if("plot"===r){var a=t,i=n;return[e[0]-a,e[1]-i,e[2]+a,e[3]+6*i]}}([Math.min.apply(null,i),Math.min.apply(null,o),Math.max.apply(null,s),Math.max.apply(null,u)],t);a.a.loadModules(["esri/geometry/Extent","esri/layers/GraphicsLayer"],r.options).then(function(e){var t=p(e,2),a=t[0],i=(t[1],new(Function.prototype.bind.apply(a,[null].concat(f(d),[new esri.SpatialReference({wkid:4326})]))));r.gismap.setExtent(i);var o=Boolean(d[2]-d[0]>.05||d[3]-d[1]>.05);n(o)})})},searchPointer:function(e){var r=this;return d(regeneratorRuntime.mark(function t(){var n,a,i,o,s,u,l,c,f,d;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return r.layersHander(),r.gismap.infoWindow.hide(),t.next=4,r.queryOnePointer(e,"dapeng");case 4:if(n=t.sent,a=p(n,2),i=a[0],o=a[1],!i){t.next=13;break}if(!(s=o.features[0].attributes.DPDKID||"")||!r.landGisIds.includes(s)){t.next=13;break}return r.$emit("gismapClickEv",{gisDkid:s}),t.abrupt("return");case 13:return t.next=15,r.queryOnePointer(e,"nongyongdi");case 15:u=t.sent,l=p(u,2),c=l[0],f=l[1],c?(d=f.features[0].attributes.DKID||"")&&r.landGisIds.includes(d)&&r.$emit("gismapClickEv",{gisDkid:d}):console.log("当前地点无地块数据");case 20:case"end":return t.stop()}},t,r)}))()},layersHander:function(e){switch(e){case 0:this.activePlotsLayer&&this.activePlotsLayer.clear();break;default:this.activePlotsLayer&&this.activePlotsLayer.clear(),this.gismap.infoWindow.hide()}},queryOnePointer:function(e,r){var t=this;return new Promise(function(n){a.a.loadModules(["esri/tasks/QueryTask","esri/tasks/query","esri/symbols/SimpleFillSymbol","esri/symbols/SimpleLineSymbol"],t.options).then(function(a){var i=p(a,4),o=i[0],s=i[1],u=i[2],l=i[3],c=new s;c.returnGeometry=!0,c.outFields=["*"];new u(u.STYLE_SOLID,new l(l.STYLE_SOLID,new dojo.Color([255,255,255]),4),new dojo.Color([255,255,255,.5]));var f,g=new o(t.serviceMap[r]+"/0?token="+t.temptoken);c.geometry=e.mapPoint,g.execute(c,(f=d(regeneratorRuntime.mark(function e(r){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:r&&r.features&&r.features.length>0&&r.features[0].attributes&&(r.features[0].attributes.hasOwnProperty("DPDKID")||r.features[0].attributes.hasOwnProperty("DKID"))?n([!0,r]):n([!1,null]);case 1:case"end":return e.stop()}},e,this)})),function(e){return f.apply(this,arguments)}))})})},showAreaInfo:function(e,r,t){var n=this;if(r.features&&0!=r.features.length){var a=r.features[0].attributes;a.hasOwnProperty("DPDKID")?e.infoWindow.setTitle("大棚: "+a.DPDKID):e.infoWindow.setTitle("农用地: "+a.DKID);var i='<div class="plot-table-content">';for(var o in a){var s=a[o];"Shape_Area"===o?s=p(a.Shape_Area):"SHAPE_Area"===o&&(s=p(a.SHAPE_Area));var l=new RegExp("[\\u4E00-\\u9FFF]+","g");if(u.a.hasOwnProperty(o)||l.test(o)){var c=u.a.hasOwnProperty(o)?u.a[o]:o;s="地块类型"===c&&u.b.hasOwnProperty(s)?u.b[s]:s,s="主体类型"===c&&u.d.hasOwnProperty(s)?u.d[s]:s,a[o]&&""!==a[o]&&" "!==a[o]&&"  "!==a[o]&&(i+='<div><span class="title pyc">'+c+"</span><p>"+s+"</p></div>")}}return i+="</div>",e.infoWindow.setContent(i),e.infoWindow.show(t,e.getInfoWindowAnchor(t)),e.infoWindow.domNode.querySelector(".titleButton.close").addEventListener("click",function(){n.layersHander()}),!0}return!1;function p(e){/\d+e[+-]\d/g.test(e=e)||e<1e-4?e*=16e6:e=parseFloat(e/666.66666666667);var r=e.toExponential().match(/\d(?:\.(\d*))?e([+-]\d+)/);return e.toFixed(Math.max(0,(r[1]||"").length-r[2]))}},getNowAreaColor:function(e,r){if(!e||!e.attributes||!(e.attributes["土地类型"]||e.attributes.TYPE||e.attributes.LANDTYPE))return[[51,98,2],[255,0,0]];var t=e.attributes["土地类型"]||e.attributes.TYPE||e.attributes.LANDTYPE;return u.c.hasOwnProperty(t)?e.attributes["土地类型"]?1===r?[u.c[t],[255,0,0]]:2===r?[u.c[t],[215,116,85]]:[u.c[t],u.c[t]]:1===r?[u.c[t],[255,0,0]]:2===r?[u.c[t],[215,116,85]]:[u.c[t],[165,165,165]]:[[201,242,208],[165,165,165]]},renderPlotToMap:function(e){var r,t=this,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"";return new Promise((r=d(regeneratorRuntime.mark(function r(a){var i,o,s,u,l,c;return regeneratorRuntime.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:return i=e.map(function(e){return t.plotidMapImg[e.gisPlotId]=e.imgUrl,e.gisPlotId}),r.next=3,t.goMorePlotsWithId("nongyongdi",i,n);case 3:return o=r.sent,s=p(o,2),u=s[0],l=s[1],c=[],u&&l.length>0&&c.push.apply(c,f(l)),r.next=11,t.renderAllPolygon(c,t.allPlotPolygonLayer,2);case 11:return r.next=13,t.renderAllMarker(c,t.allPlotMarkerLayer,17);case 13:if(!u){r.next=18;break}return r.next=16,t.getCenterAZoom(c);case 16:r.next=19;break;case 18:t.tipsShow=!0;case 19:a(c);case 20:case"end":return r.stop()}},r,t)})),function(e){return r.apply(this,arguments)}))},goMorePlotsWithId:function(e,r){var t=this,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";return d(regeneratorRuntime.mark(function a(){return regeneratorRuntime.wrap(function(a){for(;;)switch(a.prev=a.next){case 0:return a.abrupt("return",new Promise(function(){var a=d(regeneratorRuntime.mark(function a(o){var s,u,l,c;return regeneratorRuntime.wrap(function(a){for(;;)switch(a.prev=a.next){case 0:if(c=function e(r,t){return r.length>t?[r.splice(0,t)].concat(f(e(r,t))):[r]},r&&0!==r.length){a.next=4;break}return o(),a.abrupt("return");case 4:s=n&&i.a[n]&&i.a[n][e]||t.serviceMap[e],u=s+"/0?token="+t.temptoken,l=[],c(JSON.parse(JSON.stringify(r)),1e3).forEach(function(){var r=d(regeneratorRuntime.mark(function r(n,a){return regeneratorRuntime.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:l.push(t.serverQuery(u,t.plotQueryfn(n,e)));case 1:case"end":return r.stop()}},r,t)}));return function(e,t){return r.apply(this,arguments)}}()),Promise.all(l).then(function(e){var r=!1,t=[];e.forEach(function(e,n){var a=p(e,2),i=a[0],o=a[1];i&&(r=!0),t.push.apply(t,f(o))}),o([r,t])});case 10:case"end":return a.stop()}},a,t)}));return function(e){return a.apply(this,arguments)}}()));case 1:case"end":return a.stop()}},a,t)}))()},serverQuery:function(e,r){var t=this;return new Promise(function(n){a.a.loadModules(["esri/map","esri/layers/ArcGISDynamicMapServiceLayer","esri/tasks/QueryTask","esri/toolbars/draw","esri/tasks/query","esri/symbols/SimpleLineSymbol","esri/symbols/SimpleFillSymbol"],t.options).then(function(t){var a=p(t,7),i=(a[0],a[1],a[2]),o=(a[3],a[4]),s=(a[5],a[6],new i(e)),u=new o;if(u.outFields=["*"],r&&(u.where=r()),u.where){u.outSpatialReference=esri.spatialReference,u.spatialRelationship=o.SPATIAL_REL_INTERSECTS,u.returnGeometry=!0,u.returnDistinctValues=!1,u.relationParam=!1;try{s.execute(u,function(e){e.features&&0!==e.features.length?n([!0,e.features]):n([!1,[]])})}catch(e){n([!1,[]])}}else n([!1,[]])})})},plotQueryfn:function(e,r){var t="DPDKID",n=e||[];return n=n.filter(function(e){if(e)return e}),"nongyongdi"===r&&(t="DKID"),function(){for(var e="",r=0;r<n.length;r++)n[r]&&(r===n.length-1?e+=t+" = '"+n[r]+"'":e+=t+" = '"+n[r]+"' or ");return e}},greenCertLandActive:function(){var e,r=this,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[];return new Promise((e=d(regeneratorRuntime.mark(function e(n){var a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(r.greenCertPlotsIsActive=Boolean(t.length),r.greenCertPlotsLayer.clear(),r.allPlotPolygonLayer.plotFeatures&&0!==r.allPlotPolygonLayer.plotFeatures.length){e.next=5;break}return n(!1),e.abrupt("return");case 5:if(!t.length){e.next=15;break}return e.next=8,r.updateFeature(t,r.allPlotPolygonLayer.plotFeatures,r.greenCertPlotsLayer,{stroke:[255,255,255],fillOpacity:.6,fill:[118,255,3]});case 8:if(!(a=e.sent)){e.next=12;break}return e.next=12,r.getCenterAZoom(r.greenCertPlotsLayer.graphics);case 12:n(a),e.next=16;break;case 15:n(!0);case 16:case"end":return e.stop()}},e,r)})),function(r){return e.apply(this,arguments)}))},greenCertLandCanvelActive:function(){var e=this;this.greenCertPlotsIsActive&&(this.greenCertPlotsLayer._div.rawNode.querySelectorAll("path")[0]&&(a.a.loadModules(["esri/symbols/SimpleFillSymbol","esri/symbols/SimpleLineSymbol","esri/Color"],this.options).then(function(r){var t=p(r,3),n=t[0],a=t[1],i=t[2],o=new n(n.STYLE_SOLID,new a(a.STYLE_SOLID,new i([118,255,3]),3),new i([118,255,3,.6]));e.greenCertPlotsLayer.graphics.map(function(e){e.setSymbol(o)})}),this.greenCertPlotsIsActive=!1))},cropLandActiveRender:function(){var e,r=this,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],n=arguments[1];return new Promise((e=d(regeneratorRuntime.mark(function e(a){var i,o;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return r.activePlotsLayer.clear(),e.next=3,r.updateFeature(t,r.allPlotPolygonLayer.plotFeatures,r.activePlotsLayer,{stroke:[255,255,255],fillOpacity:.6});case 3:if(i=e.sent,!t.length||!i){e.next=9;break}return o=n?"plot":"company",r.activePlotsLayer.graphics[0]._extent,e.next=9,r.getCenterAZoom(r.activePlotsLayer.graphics,o);case 9:r.greenCertLandCanvelActive(),a(i);case 11:case"end":return e.stop()}},e,r)})),function(r){return e.apply(this,arguments)}))},setPlotPosition:function(e){var r=this;a.a.loadModules(["esri/map","esri/layers/ArcGISTiledMapServiceLayer","esri/layers/ArcGISDynamicMapServiceLayer","esri/layers/ImageParameters","esri/geometry/Point","esri/SpatialReference","esri/geometry/Extent","esri/layers/GraphicsLayer"],this.options).then(function(t){var n=p(t,8),a=(n[0],n[1],n[2],n[3],n[4],n[5],n[6]),i=(n[7],new(Function.prototype.bind.apply(a,[null].concat(f(e),[new esri.SpatialReference({wkid:4326})]))));r.gismap.setExtent(i,!0)})},getNYDid:function(e){return/(\d{18})(\d{3})/g.test(e)?RegExp.$1+"000":e+""}},components:{iknow:l.default}},m=t("W5g0");var h=function(e){t("SdNZ")},y=Object(m.a)(g,function(){var e=this,r=e.$createElement,t=e._self._c||r;return t("div",{staticClass:"arcgis-map"},[t("div",{staticClass:"map-container",attrs:{id:"gismap"}}),e._v(" "),e.tipsShow?t("iknow",{attrs:{tipsShow:e.tipsShow,tipText:"无法显示地块轮廓，该基地的地块未上图"},on:{"update:tipsShow":function(r){e.tipsShow=r},"update:tips-show":function(r){e.tipsShow=r}}}):e._e()],1)},[],!1,h,"data-v-dc4ea0fc",null);r.default=y.exports}});
//# sourceMappingURL=84.a95d04f6b8fb7cb1680a.js.map