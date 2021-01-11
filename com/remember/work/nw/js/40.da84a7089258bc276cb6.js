webpackJsonp([40],{WYmx:function(e,t){},x3Do:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=r("xk5x"),o=r("VCTt"),a=r("VKKs");function i(e){return function(){var t=e.apply(this,arguments);return new Promise(function(e,r){return function n(o,a){try{var i=t[o](a),c=i.value}catch(e){return void r(e)}if(!i.done)return Promise.resolve(c).then(function(e){n("next",e)},function(e){n("throw",e)});e(c)}("next")})}}var c={title:{show:!1,text:"暂无数据",textStyle:{fontSize:12,color:"#6DC1CB"},left:"center",top:"center"},grid:{show:!0,borderColor:"#0D394A",bottom:30,top:40,right:20},tooltip:{show:!0,trigger:"axis",formatter:function(e){var t=e.map(function(e){return e.seriesName+"："+(null!==e.data?Object(o.j)({value:e.data})+"元/公斤":"无")});return e[0].axisValue+"<br/>"+t.join("<br />")},backgroundColor:"#043250",padding:[13,14,13,11],textStyle:{fontSize:12,color:"#9ED2D8"},confine:!0},color:["#DC6CFE","#00E676","#F6A82B","#00D7E0"],legend:{show:!0,type:"plain",textStyle:{color:"#6DC1CB",fontSize:12},backgroundColor:"rgba(255, 255, 255, 0)",top:3,right:16,itemWidth:6,itemHeight:6,itemGap:14,height:20,icon:"circle",borderColor:"yellow"},xAxis:{data:["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"],boundaryGap:!1,axisLabel:{formatter:function(e){return e.replace(/([\d]*)[年]([\d]*)[月]([\d]*)[日]/g,"$2月$3日")},textStyle:{color:"#6DC1CB",fontSize:12},align:"center"},axisTick:{show:!1},axisLine:{show:!0,lineStyle:{color:"rgba(109,193,203,0.2)"}},z:10},yAxis:{name:"(元/公斤)",nameTextStyle:{fontSize:12,color:"#6DC1CB",padding:[4,8,5,10]},axisLine:{show:!1,lineStyle:{color:"#0D394A"}},axisTick:{show:!1},splitLine:{show:!0,lineStyle:{color:"rgba(109,193,203,0.2)"}},axisLabel:{textStyle:{color:"#6DC1CB",fontSize:12}}},series:[{name:"田头价",data:[],type:"line",smooth:!0,symbolSize:0,connectNulls:!0,areaStyle:{color:{type:"linear",x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:"rgba(233,128,251, 0.5)"},{offset:1,color:"rgba(233,128,251, 0)"}],global:!1}},lineStyle:{color:"#DC6CFE"}},{name:"批发价",data:[],type:"line",smooth:!0,symbolSize:0,connectNulls:!0,areaStyle:{color:{type:"linear",x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:"rgba(0,230,118, 0.5)"},{offset:1,color:"rgba(0,230,118, 0)"}],global:!1}},lineStyle:{color:"#00E676"}},{name:"零售价",data:[],type:"line",smooth:!0,symbolSize:0,connectNulls:!0,areaStyle:{color:{type:"linear",x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:"rgba(212, 167, 84, 0.5)"},{offset:1,color:"rgba(212, 167, 84, 0)"}],global:!1}},lineStyle:{color:"#F6A82B"}},{name:"电商价",data:[],type:"line",smooth:!0,symbolSize:0,connectNulls:!0,areaStyle:{color:{type:"linear",x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:"rgba(0,162,255, 0.5)"},{offset:1,color:"rgba(0,162,255, 0)"}],global:!1}},lineStyle:{color:"#00D7E0"}}]},s=Object(a.b)("govGovernmentSubjectVO"),l=(Object(a.b)("vegetableVariety"),(new Date).setDate((new Date).getDate()-1)),u=Object(o.c)(l,"yyyy-MM-dd"),p=Object(o.c)(u.split("-").map(function(e,t){var r=Number(e);return 0===t&&(r-=1),r}).join("/"),"yyyy-MM-dd"),d={name:"market-supervision-23",props:{farmAreaInfo:{type:Object,default:function(){return Object(o.b)()}}},data:function(){return{chart:null,loading:!1,priceTypeList:[{name:"田头价",id:0},{name:"批发价",id:1}],vegetableVariety:[],cropId:null}},mounted:function(){this.initPage()},methods:{getTtjCropList:function(){return this.$ajax.post(this.$api.operate.ttjCropList,{pageNo:1,pageSize:1e4}).then(function(e){var t=e.data;if(0===t.respCode)return t.obj;throw new Error(t)}).catch(function(e){throw console.log(e),e})},getCropPriceStatisticListWithAllPriceType:function(){return this.$ajax.post(this.$api.operate.cropPriceStatisticListWithAllPriceType,{provinceId:s.provinceId,cropId:this.cropId,startDateStr:p,endDateStr:u,statisticType:1}).then(function(e){var t=e.data;if(0===t.respCode)return t.obj;throw new Error(t)}).catch(function(e){throw e})},processTtjCropList:function(){var e=this;return i(regeneratorRuntime.mark(function t(){var r;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,e.getTtjCropList();case 3:r=t.sent,e.vegetableVariety=r.list.map(function(e){return{crop:e.cropName,cropId:e.id}}),e.cropId=e.vegetableVariety[0].cropId,t.next=12;break;case 8:throw t.prev=8,t.t0=t.catch(0),console.log(t.t0),t.t0;case 12:case"end":return t.stop()}},t,e,[[0,8]])}))()},processCropPriceStatisticListWithAllPriceType:function(){var e=this;return i(regeneratorRuntime.mark(function t(){var r,n,o;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,e.getCropPriceStatisticListWithAllPriceType();case 3:r=t.sent,n=r.length-1;case 5:if(!(n>=0)){t.next=14;break}if(o=r[n],!(null!==o.ebusinessAveragePrice||null!==o.lotAveragePrice||null!==o.retailAveragePrice||null!==o.ttjAveragePrice)){t.next=10;break}return t.abrupt("break",14);case 10:r.pop();case 11:n--,t.next=5;break;case 14:return t.abrupt("return",r);case 17:throw t.prev=17,t.t0=t.catch(0),console.log(t.t0),t.t0;case 21:case"end":return t.stop()}},t,e,[[0,17]])}))()},updateChart:function(){var e=this;return i(regeneratorRuntime.mark(function t(){var r,n;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,e.processCropPriceStatisticListWithAllPriceType();case 3:r=t.sent,n=r.reduce(function(e,t){return e[0].push(t.statisticDate),e[1].push(t.ttjAveragePrice),e[2].push(t.lotAveragePrice),e[3].push(t.retailAveragePrice),e[4].push(t.ebusinessAveragePrice),e},[[],[],[],[],[]]),e.chart.setOption({xAxis:{data:n[0]},series:[{data:n[1]},{data:n[2]},{data:n[3]},{data:n[4]}]}),t.next=12;break;case 8:throw t.prev=8,t.t0=t.catch(0),console.log(t.t0),t.t0;case 12:case"end":return t.stop()}},t,e,[[0,8]])}))()},initPage:function(){var e=this;return i(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return e.chart=e._initEcharts(e.eContainerRef,c),t.next=3,e.updateCropList();case 3:e.updateCropPrice(),e.adaptationChart(),window.addEventListener("resize",e.adaptationChart),e.$once("hook:beforeDestroy",function(){window.removeEventListener("resize",this.adaptationChart)});case 7:case"end":return t.stop()}},t,e)}))()},updateCropPrice:function(){var e=this;return i(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return e.loading=!0,t.next=3,e.updateChart();case 3:e.loading=!1;case 4:case"end":return t.stop()}},t,e)}))()},updateCropList:function(){var e=this;return i(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return e.vegetableVariety=[],t.next=3,e.processTtjCropList();case 3:case"end":return t.stop()}},t,e)}))()},selectCrop:function(){var e=this;this.chart.setOption({series:[{data:[]},{data:[]},{data:[]},{data:[]}]}),this.updateCropPrice(),this.$nextTick(function(){e.$refs.cropSearch.blur()})},checkCropReload:function(){var e=Object(a.b)("cropTime");if(!e)return!0;e=Number(e);var t=new Date(e).getMonth();return new Date(e).setMonth(t+1,1)>=(new Date).getTime()},_initEcharts:function(e,t){var r=this.$echarts.init(e);return r.setOption(t),r},adaptationChart:function(){(document.documentElement.clientWidth||document.body.clientWidth)>3e3?this.chart&&this.chart.setOption({tooltip:{textStyle:{fontSize:14}},yAxis:{nameTextStyle:{fontSize:14},axisLabel:{textStyle:{fontSize:14}}},xAxis:{axisLabel:{textStyle:{fontSize:14}}},legend:{textStyle:{fontSize:16},itemWidth:8,itemHeight:8}}):this.chart&&this.chart.setOption({tooltip:{textStyle:{fontSize:12}},yAxis:{nameTextStyle:{fontSize:12},axisLabel:{textStyle:{fontSize:12}}},xAxis:{axisLabel:{textStyle:{fontSize:12}}},legend:{textStyle:{fontSize:12},itemWidth:6,itemHeight:6}})},refreshRender:function(){this.chart&&this.chart.resize()}},computed:{eContainerRef:function(){return this.$refs.EContainer}},components:{areaPanel:n.default}},f=r("W5g0");var h=function(e){r("WYmx")},g=Object(f.a)(d,function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],staticClass:"market-supervision-20",attrs:{"element-loading-spinner":"iconfont icon-loading1","element-loading-background":"rgba(0, 0, 0, 0.2)"}},[r("area-panel",{attrs:{"area-title":"价格监测",titleLeft:""}},[r("div",{staticClass:"sub-title",attrs:{slot:"subTitle"},slot:"subTitle"},[r("el-select",{ref:"cropSearch",staticClass:"vegetable-select two",attrs:{slot:"subTitle",placeholder:"请选择",filterable:""},on:{change:e.selectCrop},slot:"subTitle",model:{value:e.cropId,callback:function(t){e.cropId=t},expression:"cropId"}},e._l(e.vegetableVariety,function(e,t){return r("el-option",{key:t,attrs:{label:e.crop,value:e.cropId}})}),1)],1),e._v(" "),r("div",{directives:[{name:"show",rawName:"v-show",value:!e.loading,expression:"!loading"}],staticClass:"main-panel",attrs:{slot:"panelMain"},slot:"panelMain"},[r("div",{ref:"EContainer",staticClass:"echart-container"})])])],1)},[],!1,h,"data-v-2b7cd559",null);t.default=g.exports}});
//# sourceMappingURL=40.da84a7089258bc276cb6.js.map