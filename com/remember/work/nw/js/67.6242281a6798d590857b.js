webpackJsonp([67],{"0McH":function(t,e){},cafx:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=a("+Yef"),n={310151:"310230"},s=a("Wftt"),i=a("VCTt"),o=a("VKKs"),c={310000:310100},l={310230:310151},m=function(t){return l[t]||t},u=a("Xtqa"),f=a("c65A"),h=(a("Wj7t"),function(){return function(t,e){if(Array.isArray(t))return t;if(Symbol.iterator in Object(t))return function(t,e){var a=[],r=!0,n=!1,s=void 0;try{for(var i,o=t[Symbol.iterator]();!(r=(i=o.next()).done)&&(a.push(i.value),!e||a.length!==e);r=!0);}catch(t){n=!0,s=t}finally{try{!r&&o.return&&o.return()}finally{if(n)throw s}}return a}(t,e);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}());function p(t){return function(){var e=t.apply(this,arguments);return new Promise(function(t,a){return function r(n,s){try{var i=e[n](s),o=i.value}catch(t){return void a(t)}if(!i.done)return Promise.resolve(o).then(function(t){r("next",t)},function(t){r("throw",t)});t(o)}("next")})}}var d=["#F0C87B","#A6D889","#DD90CB","#9173FE","#4DCBFF","#1DE9B6","#ca8622","#bda29a","#6e7074","#546570","#c4ccd3"],v={grid:{show:!0,borderColor:"#0D394A",bottom:32,left:45,right:20},color:d,tooltip:{show:!0,trigger:"item",textStyle:{fontSize:12,color:"#ffffff"},formatter:function(t){return t.name+"<br/>"+Object(i.j)({value:t.value})}},xAxis:{data:[],axisLabel:{textStyle:{color:"#6DC1CB",fontSize:12},align:"center"},axisTick:{show:!1},axisLine:{show:!0,lineStyle:{color:"#0D394A"}},z:10},yAxis:{name:"单位：",nameTextStyle:{fontSize:14,color:"#6DC1CB",padding:[0,0,10,0]},axisLine:{show:!1,lineStyle:{color:"#0D394A"}},axisTick:{show:!1},splitLine:{show:!0,lineStyle:{color:"#0D394A"}},axisLabel:{textStyle:{color:"#6DC1CB",fontSize:12}}},series:[{type:"bar",barWidth:24,data:[]}]},b=function(t){for(var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"yyyy.MM",a=(new Date).setDate(1),r=new Date(a).getFullYear(),n=[],s=0;s<6;s++)n.push("add"===t?Object(i.c)(new Date(a).setFullYear(r++),e):Object(i.c)(new Date(a).setFullYear(r--),e));return n},g={tooltip:{show:!1,trigger:"item",backgroundColor:"rgba(0, 0, 0, .9)",textStyle:{color:"#ffffff"}},geo:{map:this.mapName,label:{normal:{show:!1},emphasis:{show:!1}},roam:!1,aspectScale:.9,itemStyle:{normal:{areaColor:"rgba(4, 119, 145, .0)",borderColor:"rgba(0, 248, 255, .0)"},emphasis:{areaColor:"rgba(4, 119, 145, .0)"}},zoom:.9},series:[{name:this.mapName,type:"map",map:this.mapName,label:{normal:{show:!1},emphasis:{show:!1}},roam:!1,aspectScale:.9,itemStyle:{normal:{areaColor:"rgba(4, 119, 145, .8)",borderColor:"rgba(0, 248, 255, .8)"},emphasis:{areaColor:"rgba(4, 119, 145, .8)"}},tooltip:{show:!1},zoom:.9},{name:this.mapName,type:"scatter",coordinateSystem:"geo",label:{show:!0,formatter:function(t){return Number(t.value[2])>1e3?"99+":t.value[2]},color:"#fff",fontSize:12,offset:[0,-2],emphasis:{show:!1}},zlevel:2,symbol:"image://"+a("o0r7"),symbolSize:[24,30],itemStyle:{color:"transparent",opacity:1},data:[]}]},y=Object(i.b)(),C={name:"operators",data:function(){return{checkAttestChart:null,checkAttestDialogVisible:!1,getYear:i.k,checkAttestSelected:2,flowDateRange:{disabledDate:function(t){return!(t<(new Date).setDate(1))}},checkAttestTableData:null,checkAttestTable:null,checkAttestThead:["检测次数","检测报告"],checkAttestDes:"进行环境检测的基地",checkAttestNum:0,farmDistribution:null,numberOfFarms:0,coveringLandArea:0,allLandArce:0,allLandArceOnPlanting:0,mapChart:null,cityTags:[],mapId:(t=y.farmAreaId,c[t]||t),mapLevel:y.farmAreaType+Number(!!c[y.farmAreaId]),mapName:y.farmAreaName,hasNextLevel:!1,isUseCacheTags:!1,farmActivityTable:null,farmActivityDate:[],farmSele:"all",farmColName:"上次上报数据",rankingTable:null,rankingTableFarmWidth:150,rankingTableDate:null,rankingYears:[(new Date).getTime(),(new Date).setFullYear((new Date).getFullYear()-1),(new Date).setFullYear((new Date).getFullYear()-2)],viewsPic:[],showViews:!1,isInGoingLevel:!1,searchFarmStr:"",searchHasResult:!0,businessCategoryList:[],businessCategoryStatistics:[],isShanghaiRegulatoryArea:!1,farmlistLoader:!0};var t},watch:{searchFarmStr:function(t){var e=this;this.searchHasResult=!1,this.farmActivityDate.forEach(function(a){-1!==a.farmName.indexOf(t)?(a.nohas=!1,e.searchHasResult=!0):a.nohas=!0}),this.$nextTick(function(){e.farmActivityTable.scrollTo(0,0,10),e.farmActivityTable.refresh()})}},filters:{numTofixed:u.b},created:function(){var t=this,e=Object(o.b)("govGovernmentSubjectVO"),a=e.countyId||e.cityId||e.provinceId;this.isShanghaiRegulatoryArea=/^310\d{3}$/g.test(a),this.getFarmStatistics(),this.$nextTick(p(regeneratorRuntime.mark(function e(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:t.doSwitchFarmActive("all"),t.initBaseScatter(),t.checkAttestChart=t.initEcharts(t.$refs.checkAttestChart,v),t.checkAttestChart.on("click",function(e){t.getYear=new Date(""+Object(i.c)(e.name,"yyyy")),t.checkAttestDialogVisible=!0,t.getCheckAttestTable({reportType:"环境检测"===e.seriesName?2:1})}),t.getCheckAttestChart().then(function(e){t.setCheckAttestChart(e)}),t.rankingTable=Object(i.a)(t.$refs.rankingTable.$el.querySelector(".el-table__body-wrapper")),t.getrankingTable(),t.setWidthFarmWidth();case 8:case"end":return e.stop()}},e,t)})))},mounted:function(){var t=this;window.onresize=function(){t.mapChart.resize(),t.checkAttestChart.resize(),t.setWidthFarmWidth()}},methods:{initBaseScatter:function(){var t=this;return p(regeneratorRuntime.mark(function e(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return t.mapChart=t.initEcharts(t.$refs.mapChart,g),t.mapChart.showLoading({text:"loading",color:"#00F6FF",textColor:"#00F6FF",maskColor:"rgba(0, 246, 255, 0)",fontSize:16,spinnerRadius:18,zlevel:0}),t.callbackPageInitMap(),t.bindGeoRoam(),o.a.get("cityTags")||[],t.addTags(),e.next=8,t.initAreaOutlineAndPointer(t.mapLevel,t.mapId);case 8:t.mapChart.hideLoading(),t.handleClickEvent();case 10:case"end":return e.stop()}},e,t)}))()},initAreaOutlineAndPointer:function(t,e){var a,r=this;return new Promise((a=p(regeneratorRuntime.mark(function a(s){var i,o,c,l,m,u;return regeneratorRuntime.wrap(function(a){for(;;)switch(a.prev=a.next){case 0:return a.next=2,r.getFeaturesUpdateChart();case 2:return i=a.sent,o=i.features,c=!0,l=n[e]||e,a.next=8,r.getFarmAreaInfo(t,l);case 8:(m=a.sent).nextAreaList.length||m.farmList.length||m.businessCategoryList.length||(c=!1),r.businessCategoryList=m.businessCategoryList,r.hasNextLevel?r.addFarmPointerToMap({features:o,areaData:m.nextAreaList}):r.addFarmPointerToMap({features:o,areaData:m.farmList}),r.businessCategoryStatistics=r.businessCategoryHander(m.farmList,m.businessCategoryList),u=Boolean(m.nextAreaList.length||m.farmList.length),s({canGetAreaData:c,hasNext:u,nextAreaList:m.nextAreaList,farmList:m.farmList,businessCategoryList:m.businessCategoryList});case 15:case"end":return a.stop()}},a,r)})),function(t){return a.apply(this,arguments)}))},addFarmPointerToMap:function(t){var e=t.features,r=t.areaData,n=void 0,s=e.map(function(t){return t.properties.adcode});if(this.hasNextLevel){var i=(r=r.map(function(t){return t.coord=[t.lng,t.lat],t})).map(function(t){var e=s.includes(Number(m(t.areaId)))&&!!t.farmNum,r=e?t.coord.concat([t.farmNum,m(t.areaId)]):t.coord.concat(["",m(t.areaId)]);return{name:t.areaName,value:r,tooltip:{show:!0,formatter:function(t){return t.name}},symbol:e?"image://"+a("o0r7"):"",symbolSize:[24,30]}});n={type:"scatter",coordinateSystem:"geo",name:this.mapName,zlevel:2,roam:!1,label:{show:!0,color:"#fff",fontSize:12,offset:[0,-2],emphasis:{show:!1},formatter:function(t){return 4===t.value.length?Number(t.value[2])>1e3?"99+":t.value[2]:""}},itemStyle:{color:"transparent",opacity:1},data:i,animation:!0,markPoint:{}}}else{var o=this;n={type:"scatter",coordinateSystem:"geo",roam:!0,name:this.mapName,zlevel:2,label:{show:!1},itemStyle:{color:"transparent",opacity:1},tooltip:{show:!0,formatter:function(t){return t.name}},symbol:"path://m50.375008,136.583319c5.499999,-0.25 37.937494,-38.541659 45.187492,-64.697905c7.249999,-26.156246 5.8125,-72.34374 -45.437493,-72.218739c-51.249993,0.125001 -54.499991,42.874992 -46.281243,71.968739c8.218749,29.093746 41.031245,65.197905 46.531244,64.947905z",symbolSize:[10,10],symbolKeepAspect:!0,data:r.map(function(t,e){var a=[t.farmCenterLng,t.farmCenterLat].concat(["farm"],[t.farmId]),r=o.getBusinessCategoryColor(t.businessCategoryIdList,o.businessCategoryList);return{name:t.farmName,coord:[t.farmCenterLng,t.farmCenterLat],value:a,itemStyle:{normal:{color:r,borderColor:r},emphasis:{color:r,borderColor:r}}}}),animation:!0}}var c={animation:!0,tooltip:{show:!1},geo:{map:this.mapName,animation:!0,center:void 0,label:{normal:{show:!1},emphasis:{show:!1}},aspectScale:.9,itemStyle:{normal:{areaColor:"rgba(4, 119, 145, .0)",borderColor:"rgba(0, 248, 255, .0)"},emphasis:{areaColor:"rgba(4, 119, 145, .0)"}},zoom:.9},series:[{type:"map",name:this.mapName,map:this.mapName,zoom:.9,roam:!0,center:void 0,aspectScale:.9,itemStyle:{normal:{areaColor:"rgba(4, 119, 145, .8)",borderColor:"rgba(0, 248, 255, .8)"},emphasis:{areaColor:"rgba(4, 119, 145, .8)"}},label:{normal:{show:!1},emphasis:{show:!1}},tooltip:{show:!0,formatter:function(t){return t.name}},data:e.map(function(t){var e=t.properties.center;return{name:t.properties.name,value:e.concat(["map"],[t.id||t.properties.adcode])}})},n]};this.isInGoingLevel=!1,this.mapChart.setOption(c),this.isUseCacheTags=!1},bindGeoRoam:function(){var t=this;this.mapChart.on("georoam",function(e){var a=t.mapChart.getOption(),r=e.componentType;"series"===r&&t.mapChart.setOption({geo:{center:a.series[0].center,zoom:a.series[0].zoom}}),"geo"===r&&t.mapChart.setOption({series:[{center:a.geo[0].center,zoom:a.geo[0].zoom}]})})},callbackPageInitMap:function(){var t=o.a.get("cityTags")||[],e=t[t.length-1];0!==t.length&&(this.isUseCacheTags=!0,this.mapId=e.id,this.mapName=e.name,this.mapLevel=e.level)},getFeaturesUpdateChart:function(){var t=this;return p(regeneratorRuntime.mark(function e(){var a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(i.g)({areaId:r.a[t.mapId]||t.mapId});case 2:if(a=e.sent){e.next=7;break}return t.isInGoingLevel=!1,t.mapLevel--,e.abrupt("return");case 7:return t.$echarts.registerMap(t.mapName,{features:a.features,type:"FeatureCollection"}),t.hasNextLevel=a.sub,e.abrupt("return",a);case 10:case"end":return e.stop()}},e,t)}))()},addTags:function(){var t=o.a.get("cityTags")||[];this.isUseCacheTags?this.cityTags=t:this.cityTags.push({name:this.mapName,id:this.mapId,level:this.mapLevel})},getBusinessCategoryColor:function(t,e){var a=t||[],r="#fcf820";return a.length>1&&(r="#35e6bc"),1===a.length&&e.length&&e.map(function(t){a[0]===t.id&&(r=t.bizCategoryColor)}),r},handleClickEvent:function(){var t,e=this;this.mapChart.on("click",(t=p(regeneratorRuntime.mark(function t(a){return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:if(!e.isInGoingLevel){t.next=2;break}return t.abrupt("return",!1);case 2:if(!e.hasNextLevel){t.next=14;break}if(e.isInGoingLevel=!0,e.mapId=a.data.value[3],e.mapId){t.next=7;break}return t.abrupt("return");case 7:return e.mapName=a.name,e.mapLevel+=1,t.next=11,e.initAreaOutlineAndPointer(e.mapLevel,e.mapId);case 11:e.addTags(),t.next=15;break;case 14:"farm"===a.value[2]&&(o.a.set("cityTags",e.cityTags),e.$router.push({path:"/farmdetail/"+a.value[3]}));case 15:case"end":return t.stop()}},t,e)})),function(e){return t.apply(this,arguments)}))},handleTagClose:function(t){var e=this;return p(regeneratorRuntime.mark(function a(){var r;return regeneratorRuntime.wrap(function(a){for(;;)switch(a.prev=a.next){case 0:if(o.a.set("cityTags",""),!e.isInGoingLevel){a.next=3;break}return a.abrupt("return",!1);case 3:if(!(t>0)){a.next=12;break}return e.isInGoingLevel=!0,e.cityTags=e.cityTags.slice(0,t),r=e.cityTags[e.cityTags.length-1],e.mapId=r.id,e.mapName=r.name,e.mapLevel=r.level,a.next=12,e.initAreaOutlineAndPointer(e.mapLevel,e.mapId);case 12:case"end":return a.stop()}},a,e)}))()},getFarmStatistics:function(){var t=this;this.$ajax.post(this.$api.operators.farmStatistics,{areaId:[y.farmAreaId],farmAreaType:y.farmAreaType}).then(function(e){var a=e.data,r=void 0;0===a.respCode&&(r=a.obj,t.numberOfFarms="number"==typeof r.farmNum?r.farmNum:0,t.coveringLandArea=r.farmArce,t.allLandArce=r.allLandArce,t.allLandArceOnPlanting=r.allLandArceOnPlanting)})},viewDetail:function(t){switch(this[t]=!0,t){case"checkAttestDialogVisible":this.getYear=new Date((new Date).setDate(1)),this.getCheckAttestTable({reportType:2})}},getNotActiveFarm:function(){var t=this;return p(regeneratorRuntime.mark(function e(){var a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return a=null,e.next=3,new Promise(function(e,r){t.$ajax.post(t.$api.operators.farmNotActive,{farmAreaId:[y.farmAreaId],farmAreaType:y.farmAreaType}).then(function(t){var n=t.data;if(0===n.respCode)return n.obj=n.obj.map(function(t){return{farmId:t.farmId,farmName:t.farmName,activeDays:t.lastActiveDays}}),a=n,e(n);r(new Error("获取不活跃的基地数据错误"))})});case 3:return e.abrupt("return",a);case 4:case"end":return e.stop()}},e,t)}))()},getActiveFarm:function(){var t=this;return p(regeneratorRuntime.mark(function e(){var a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return a=null,e.next=3,new Promise(function(e,r){t.$ajax.post(t.$api.operators.farmActive,{farmAreaId:[y.farmAreaId],farmAreaType:y.farmAreaType}).then(function(t){var n=t.data;if(0===n.respCode)return a=n,e(n);r(new Error("获取活跃的基地数据错误"))})});case 3:return e.abrupt("return",a);case 4:case"end":return e.stop()}},e,t)}))()},getAllFarm:function(){var t=this;return p(regeneratorRuntime.mark(function e(){var a,r,n;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return a=JSON.parse(localStorage.govGovernmentSubjectVO),r=a.subjectLevel,n=[a.provinceId,a.provinceId,a.cityId,a.countyId],e.abrupt("return",new Promise(function(e){t.$ajax.post(t.$api.operators.listByArea,{farmAreaId:[n[r]],farmAreaType:a.subjectLevel}).then(function(t){var a=t.data;0===a.respCode&&a.obj&&a.obj.list?e(a.obj):e()})}));case 4:case"end":return e.stop()}},e,t)}))()},handleFarmData:function(t){var e=this;return p(regeneratorRuntime.mark(function a(){var r,n,s,i;return regeneratorRuntime.wrap(function(a){for(;;)switch(a.prev=a.next){case 0:r=null,a.t0=t,a.next="notActive"===a.t0?4:"active"===a.t0?9:14;break;case 4:return a.next=6,e.getNotActiveFarm();case 6:return a.t1=function(t){return{farmId:t.farmId,farmName:t.farmName,activityNum:t.activeDays+"天前"}},r=a.sent.obj.map(a.t1),a.abrupt("break",22);case 9:return a.next=11,e.getActiveFarm();case 11:return a.t2=function(t){return{farmId:t.farmId,farmName:t.farmName,activityNum:t.activeDays+"天"}},r=a.sent.obj.map(a.t2),a.abrupt("break",22);case 14:return a.next=16,e.getAllFarm();case 16:return n=a.sent,s=n.list,i=n.businessCategoryList,e.businessCategoryList=i,r=s.map(function(t,a){var r=[];if(t.businessCategoryIdList.length>0){var n=t.businessCategoryIdList[0],s={};e.businessCategoryList.map(function(t){n===t.id&&(s={name:t.bizCategoryName,color:t.bizCategoryColor||"#fcf820"})}),t.businessCategoryIdList.length>1&&(s={name:"复合",color:"#35e6bc"}),r.push(s)}return{farmName:t.farmName,farmId:t.farmId,labels:r}}),a.abrupt("break",22);case 22:return a.abrupt("return",[r,t]);case 23:case"end":return a.stop()}},a,e)}))()},doSwitchFarmActive:function(t){var e=this;return p(regeneratorRuntime.mark(function a(){var r,n,s;return regeneratorRuntime.wrap(function(a){for(;;)switch(a.prev=a.next){case 0:e.farmSele=t,e.farmActivityDate=[],e.farmlistLoader=!0,a.t0=t,a.next="notActive"===a.t0?6:"active"===a.t0?8:10;break;case 6:return e.farmColName="上次上报数据",a.abrupt("break",12);case 8:return e.farmColName="近30天上报数据天数",a.abrupt("break",12);case 10:return e.farmColName="",a.abrupt("break",12);case 12:return a.next=14,e.handleFarmData(t);case 14:if(r=a.sent,n=h(r,2),s=n[0],n[1]===e.farmSele){a.next=20;break}return a.abrupt("return");case 20:e.farmActivityDate=s,e.farmlistLoader=!1,e.$nextTick(function(){e.farmActivityTable?(e.farmActivityTable.scrollTo(0,0,10),e.farmActivityTable.refresh()):e.farmActivityTable=Object(i.a)(e.$refs.farmActivityTable)});case 23:case"end":return a.stop()}},a,e)}))()},getCheckAttestChart:function(){var t=this;return p(regeneratorRuntime.mark(function e(){var a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return a=null,e.next=3,new Promise(function(e,r){t.$ajax.post(t.$api.operators.farmInspectNum,{areaIds:[y.farmAreaId],areaType:y.farmAreaType,dateList:b("minus","yyyy-MM-dd").reverse()}).then(function(t){var n=t.data;if(0===n.respCode)return a=n,e(n);r(new Error("获取检测与认证趋势图数据错误"))})});case 3:return e.abrupt("return",a);case 4:case"end":return e.stop()}},e,t)}))()},setCheckAttestChart:function(t){var e=t.obj;this.checkAttestChart.setOption({color:[d[0],d[4]],tooltip:{show:!0,formatter:function(t){return Object(i.c)(t.name,"yyyy")+"年<br/>"+t.seriesName+"："+Object(i.l)({value:t.value,unit:"家"}).formatter+"基地"}},legend:{data:["环境检测","农产品认证"],show:!0,top:16,right:"center",height:22,itemWidth:12,itemHeight:12,textStyle:{color:"#6DC1CB",fontSize:12,lineHeight:20}},xAxis:{data:e.authNumList.map(function(t){return Object(i.c)(t.cetificateDate,"yyyy")}),axisLabel:{formatter:function(t){return t}}},yAxis:{name:"单位：家",axisLabel:{formatter:function(t){return Object(i.l)({value:t}).formatter}}},series:[{type:"bar",name:"环境检测",barWidth:14,data:e.checkNumList.map(function(t){return{name:t.cetificateDate,value:t.farmNum}})},{type:"bar",name:"农产品认证",barWidth:14,data:e.authNumList.map(function(t){return{name:t.cetificateDate,value:t.farmNum}})}]})},getCheckAttestTable:function(){var t=this,e=(arguments.length>0&&void 0!==arguments[0]?arguments[0]:{}).reportType,a=void 0===e?this.checkAttestSelected:e;switch(this.checkAttestSelected=a,a){case 1:this.checkAttestDes="进行农产品认证的基地",this.checkAttestThead=["认证次数","认证证书"];break;case 2:this.checkAttestDes="进行环境检测的基地",this.checkAttestThead=["检测次数","检测报告"]}this.$ajax.post(this.$api.operators.farmInspectNumList,{areaIds:[y.farmAreaId],areaType:y.farmAreaType,date:this.getYear.getTime(),pageNo:1,pageSize:5e3,reportType:a}).then(function(e){var a=e.data;0===a.respCode&&(t.checkAttestNum=a.obj.farmTotalNum,t.checkAttestTableData=a.obj.farmVOS.map(function(t){return{farm:t.farmName,attestNumber:t.inspectReportNum,certificate:t.imgNum,pics:t.imgUrls}}),t.$nextTick(function(){if(t.checkAttestTable)return t.checkAttestTable.refresh(),t.checkAttestTable.scrollTo(0,0,0),!0;t.checkAttestTable=Object(i.a)(t.$refs.checkAttestTable.$el.querySelector(".el-table__body-wrapper"))}))})},getrankingTable:function(){var t=this;this.$ajax.post(this.$api.operators.farmInspectRank,{areaIds:[y.farmAreaId],areaType:y.farmAreaType,dateList:this.rankingYears}).then(function(e){var a=e.data;0===a.respCode&&(t.rankingTableDate=a.obj.map(function(t){return{yearBeforeLast:t.subVOList[2].inspectNum,lastYear:t.subVOList[1].inspectNum,curYear:t.subVOList[0].inspectNum,farmName:t.farmName}}),t.$nextTick(function(){return t.rankingTable.refresh(),t.rankingTable.scrollTo(0,0,0),!0}))})},showPicsView:function(t,e,a){"certificate"===e.property&&(this.viewsPic=t.pics.split(","),this.showViews=!0)},setRankTable:function(t){var e=this,a=(t.row,t.column,t.rowIndex),r=t.columnIndex;switch(a){case 0:case 1:case 2:if(0===r)return"rank-cell";break;default:if(0===r)return this.$nextTick(function(){for(var t=e.$refs.rankingTable.$el.querySelectorAll("._rank-cell"),a=0;a<t.length;a++)t[a].querySelector(".cell").setAttribute("data-beforeContent",""+(a+4))}),"_rank-cell"}},setWidthFarmWidth:function(){if(document.body.clientWidth<1920)return this.rankingTableFarmWidth=120,!0},businessCategoryHander:function(t,e){if(!t.length||!e.length)return[];var a={fh:{name:"复合",color:"#35e6bc",num:0}};e.map(function(t){a.hasOwnProperty(t.id)||(a[t.id]={name:t.bizCategoryName,color:t.bizCategoryColor,num:0})}),t.map(function(t){var e=t.businessCategoryIdList;e.length&&(1===e.length&&a[e[0]].num++,e.length>1&&a.fh.num++)});var r=[];return e.map(function(t){a[t.id].num&&r.push(a[t.id])}),a.fh.num&&r.push(a.fh),r},unitTranslate:i.l,initEcharts:function(t,e){var a=this.$echarts.init(t);return a.setOption(e),a},getFarmAreaInfo:function(t,e){return this.$ajax.post(this.$api.operators.farmDistribution,{farmAreaType:t,farmAreaId:[e]}).then(function(t){var e=t.data;if(0===e.respCode)return e.obj})}},computed:{},components:{freetekBox:s.default,views:f.default}},A=a("W5g0");var w=function(t){a("0McH")},k=Object(A.a)(C,function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{directives:[{name:"title",rawName:"v-title"}],staticClass:"layout-container",attrs:{"data-title":"经营主体监管"}},[a("div",{staticClass:"item-container"},[a("div",{staticClass:"s-item-wrap"},[a("div",{staticClass:"_s-item-wrap"},[a("freetek-box",{attrs:{title:"基地统计"}},[a("div",{staticClass:"statistics-container"},[a("div",{staticClass:"item"},[a("p",{staticClass:"item-name"},[a("i",{staticClass:"iconfont icon-999999"}),t._v("\n\t\t\t\t\t\t\t\t基地数量\n\t\t\t\t\t\t\t")]),t._v(" "),a("p",{staticClass:"item-result"},[t._v("\n\t\t\t\t\t\t\t\t"+t._s(t.unitTranslate({unit:"家",value:t.numberOfFarms}).formatter)+"\n\t\t\t\t\t\t\t")])]),t._v(" "),t.isShanghaiRegulatoryArea?t._e():a("div",{staticClass:"item"},[a("p",{staticClass:"item-name"},[a("i",{staticClass:"iconfont icon-nongtian"}),t._v("\n\t\t\t\t\t\t\t\t覆盖土地面积\n\t\t\t\t\t\t\t")]),t._v(" "),a("p",{staticClass:"item-result"},[t._v("\n\t\t\t\t\t\t\t\t"+t._s(t.unitTranslate({unit:"亩",value:t.allLandArce}).formatter)+"\n\t\t\t\t\t\t\t")])]),t._v(" "),t.isShanghaiRegulatoryArea?a("div",{staticClass:"item itemtype"},[a("div",{staticClass:"plant-area"},[a("p",{staticClass:"value"},[t._v(t._s(t._f("numTofixed")(t.coveringLandArea/1e4,2))+"万亩")]),t._v(" "),a("p",{staticClass:"info"},[t._v("土地流转面积")])]),t._v(" "),a("div",{staticClass:"plant-area"},[a("p",{staticClass:"value"},[t._v(t._s(t._f("numTofixed")(t.allLandArce/1e4,2))+"万亩")]),t._v(" "),a("p",{staticClass:"info"},[t._v("可种植/养殖面积")])]),t._v(" "),a("div",{staticClass:"plant-area"},[a("p",{staticClass:"value"},[t._v(t._s(t._f("numTofixed")(t.allLandArceOnPlanting/1e4,2))+"万亩")]),t._v(" "),a("p",{staticClass:"info"},[t._v("在田面积")])])]):t._e()])])],1)]),t._v(" "),a("div",{staticClass:"s-item-wrap"},[a("div",{staticClass:"_s-item-wrap"},[a("freetek-box",{attrs:{showTitle:!1}},[a("div",{staticClass:"farm-table-container"},[a("div",{staticClass:"farm-tabs"},[a("div",{staticClass:"farm-tab",class:{selected:"all"===t.farmSele},on:{click:function(e){return t.doSwitchFarmActive("all")}}},[t._v("\n\t\t\t\t\t\t\t\t全部基地\n\t\t\t\t\t\t\t")]),t._v(" "),a("div",{staticClass:"farm-tab",class:{selected:"active"===t.farmSele},on:{click:function(e){return t.doSwitchFarmActive("active")}}},[t._v("\n\t\t\t\t\t\t\t\t活跃基地\n\t\t\t\t\t\t\t")]),t._v(" "),a("div",{staticClass:"farm-tab",class:{selected:"notActive"===t.farmSele},on:{click:function(e){return t.doSwitchFarmActive("notActive")}}},[t._v("\n\t\t\t\t\t\t\t\t沉默基地\n\t\t\t\t\t\t\t")])]),t._v(" "),a("div",{staticClass:"farm-table-content"},[a("div",{staticClass:"farmlist-con"},["all"===t.farmSele?a("div",{staticClass:"search"},[a("label",{attrs:{for:"searchAllFarm"}}),t._v(" "),a("input",{directives:[{name:"model",rawName:"v-model",value:t.searchFarmStr,expression:"searchFarmStr"}],attrs:{type:"text",placeholder:"搜索基地",id:"searchAllFarm",autocomplete:"off"},domProps:{value:t.searchFarmStr},on:{input:function(e){e.target.composing||(t.searchFarmStr=e.target.value)}}}),t._v(" "),t.searchFarmStr?a("span",{staticClass:"clearinput",on:{click:function(e){t.searchFarmStr=""}}}):t._e()]):t._e(),t._v(" "),"all"!==t.farmSele?a("div",{staticClass:"farm-title"},[a("span",{staticClass:"name"},[t._v("基地名称")]),t._v(" "),a("span",{staticClass:"name"},[t._v(t._s(t.farmColName))])]):t._e(),t._v(" "),a("div",{ref:"farmActivityTable",staticClass:"farmlist-items",class:{allfarmlist:"all"===t.farmSele}},["all"===t.farmSele?a("ul",{directives:[{name:"show",rawName:"v-show",value:!t.farmlistLoader,expression:"!farmlistLoader"}]},[t._l(t.farmActivityDate,function(e,r){return t.searchHasResult&&!e.nohas?a("li",{on:{click:function(a){return t.$router.push({path:"/farmdetail/"+e.farmId})}}},[a("span",{staticClass:"name"},[t._v(t._s(e.farmName))]),t._v(" "),e.labels&&e.labels.length>0?a("span",{staticClass:"labels"},t._l(e.labels,function(e,r){return a("i",{style:{color:e.color}},[t._v(t._s(e.name))])}),0):t._e(),t._v(" "),e.labels&&0!==e.labels.length?t._e():a("span",{staticClass:"labelplus",attrs:{title:"进入基地"}})]):t._e()}),t._v(" "),t.searchHasResult?t._e():a("li",{staticClass:"nodata"},[t._v("\n\t\t\t\t\t\t\t\t\t\t\t暂无搜索结果\n\t\t\t\t\t\t\t\t\t\t")])],2):t._e(),t._v(" "),"all"!==t.farmSele?a("ul",{directives:[{name:"show",rawName:"v-show",value:!t.farmlistLoader,expression:"!farmlistLoader"}]},[t._l(t.farmActivityDate,function(e,r){return t.farmActivityDate.length>0?a("li",{attrs:{name:JSON.stringify(e)},on:{click:function(a){return t.$router.push({path:"/farmdetail/"+e.farmId})}}},[a("span",{staticClass:"name"},[t._v(t._s(e.farmName))]),t._v(" "),a("span",{staticClass:"farm-data"},[t._v(t._s(e.activityNum))])]):t._e()}),t._v(" "),0===t.farmActivityDate.length?a("li",{staticClass:"nodata"},[t._v("\n\t\t\t\t\t\t\t\t\t\t\t暂无数据\n\t\t\t\t\t\t\t\t\t\t")]):t._e()],2):t._e(),t._v(" "),t.farmlistLoader?a("div",{directives:[{name:"loading",rawName:"v-loading",value:t.farmlistLoader,expression:"farmlistLoader"}],staticClass:"farmlisttab-loader",attrs:{"element-loading-text":"加载中...","element-loading-spinner":"el-icon-loading","element-loading-background":"rgba(0, 0, 0, 0)"}}):t._e()])])])])])],1)])]),t._v(" "),a("div",{staticClass:"b-item-wrap"},[a("div",{staticClass:"_b-item-wrap"},[a("freetek-box",{attrs:{title:"基地分布",size:"big"}},[a("div",{staticClass:"tags-bar"},t._l(t.cityTags,function(e,r){return a("el-tag",{directives:[{name:"show",rawName:"v-show",value:0!==r,expression:"index !== 0"}],key:r,attrs:{closable:0!==r,"disable-transitions":!1},on:{close:function(e){return t.handleTagClose(r)}}},[t._v("\n\t\t\t\t\t\t"+t._s(e.name)+"\n\t\t\t\t\t")])}),1),t._v(" "),a("div",{ref:"mapChart",staticClass:"map-container"})]),t._v(" "),t.businessCategoryStatistics.length?a("div",{staticClass:"base-type-map"},t._l(t.businessCategoryStatistics,function(e,r){return a("span",{key:r},[a("i",{style:{"background-color":e.color}}),t._v(t._s(e.name)+"："+t._s(e.num||0)+"家")])}),0):t._e()],1)]),t._v(" "),a("div",{staticClass:"item-container"},[a("div",{staticClass:"s-item-wrap"},[a("div",{staticClass:"_s-item-wrap"},[a("freetek-box",{attrs:{title:"检测与认证趋势图"}},[a("div",{staticClass:"chart-item-wrap"},[a("div",{ref:"checkAttestChart",staticClass:"chart-item"}),t._v(" "),a("el-button",{staticClass:"view-detail",attrs:{type:"text"},on:{click:function(e){return t.viewDetail("checkAttestDialogVisible")}}},[t._v("\n\t\t\t\t\t\t\t明细\n\t\t\t\t\t\t\t"),a("i",{staticClass:"el-icon-d-arrow-right"})])],1)])],1)]),t._v(" "),a("div",{staticClass:"s-item-wrap"},[a("div",{staticClass:"_s-item-wrap"},[a("freetek-box",{attrs:{title:"检测与认证排名"}},[a("div",{staticClass:"ranking-table-container"},[a("el-table",{ref:"rankingTable",attrs:{data:t.rankingTableDate,stripe:"",height:"100%",width:"100%","cell-class-name":t.setRankTable}},[a("el-table-column",{attrs:{prop:"farmName","show-overflow-tooltip":"",align:"left",width:t.rankingTableFarmWidth,label:"基地名称"}}),t._v(" "),a("el-table-column",{attrs:{prop:"yearBeforeLast",align:"center",width:"60",label:t._f("dateFormat")(t.rankingYears[2],"yyyy")}}),t._v(" "),a("el-table-column",{attrs:{prop:"lastYear",align:"center",width:"60",label:t._f("dateFormat")(t.rankingYears[1],"yyyy")}}),t._v(" "),a("el-table-column",{attrs:{prop:"curYear",align:"center",width:"60",label:t._f("dateFormat")(t.rankingYears[0],"yyyy")}})],1)],1)])],1)])]),t._v(" "),a("el-dialog",{attrs:{visible:t.checkAttestDialogVisible,"show-close":!0,"close-on-click-modal":!1,top:"calc((100vh - 580px) / 2)","custom-class":"detail-dialog"},on:{"update:visible":function(e){t.checkAttestDialogVisible=e}}},[a("freetek-box",{attrs:{title:"环境检测",showTitle:!1,size:"big"}},[a("div",{staticClass:"dialog-table-container"},[a("div",{staticClass:"dialog-tabs"},[a("div",{staticClass:"dialog-tab",class:{selected:2===t.checkAttestSelected},on:{click:function(e){return t.getCheckAttestTable({reportType:2})}}},[t._v("\n\t\t\t\t\t\t环境检测\n\t\t\t\t\t")]),t._v(" "),a("div",{staticClass:"dialog-tab",class:{selected:1===t.checkAttestSelected},on:{click:function(e){return t.getCheckAttestTable({reportType:1})}}},[t._v("\n\t\t\t\t\t\t农产品认证\n\t\t\t\t\t")])]),t._v(" "),a("div",{staticClass:"dialog-table-content"},[a("div",{staticClass:"head-info"},[a("el-date-picker",{attrs:{type:"year",format:"yyyy年","picker-options":t.flowDateRange,clearable:!1,placeholder:"选择年"},on:{change:function(e){return t.getCheckAttestTable()}},model:{value:t.getYear,callback:function(e){t.getYear=e},expression:"getYear"}}),t._v(" "),a("p",{staticClass:"yield-info"},[t._v("\n\t\t\t\t\t\t\t"+t._s(t._f("dateFormat")(t.getYear,"yyyy年"))+t._s(t.checkAttestDes)+"："),a("span",[t._v(t._s(t.checkAttestNum)+"家")])])],1),t._v(" "),a("div",{staticClass:"table-container"},[a("el-table",{ref:"checkAttestTable",attrs:{data:t.checkAttestTableData,stripe:"",height:"100%",width:"100%","cell-class-name":"check-attest"},on:{"cell-click":t.showPicsView}},[a("el-table-column",{attrs:{prop:"farm",label:"基地"}}),t._v(" "),a("el-table-column",{attrs:{prop:"attestNumber",label:t.checkAttestThead[0],width:"160px"}}),t._v(" "),a("el-table-column",{attrs:{prop:"certificate",label:t.checkAttestThead[1],align:"center",width:"160px"}})],1)],1)])])])],1),t._v(" "),t.showViews?a("views",{attrs:{"show-arrow":!0,pics:t.viewsPic},on:{viewerListen:function(e){t.showViews=!1}}}):t._e()],1)},[],!1,w,"data-v-fd4e3044",null);e.default=k.exports},o0r7:function(t,e){t.exports="https://snkoudai.oss-cn-hangzhou.aliyuncs.com/goverment/static/img/_ico_pos.f3c59aa.png"}});
//# sourceMappingURL=67.6242281a6798d590857b.js.map