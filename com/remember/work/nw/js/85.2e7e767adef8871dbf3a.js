webpackJsonp([85],{"77zU":function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=a("446f"),n=a("XPi1"),s=(a("VCTt"),a("VKKs")),o=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var a=arguments[e];for(var i in a)Object.prototype.hasOwnProperty.call(a,i)&&(t[i]=a[i])}return t},r=(Object(s.b)("govGovernmentSubjectVO"),["#D5EF10","#F6A82B","#32CEBB","#10AC2A","#3649FB","#CB4A99"]),l={title:{show:!1,left:"center",top:"35%",textStyle:{color:"#9ED2D8",fontSize:12,lineHeight:22},subtextStyle:{color:"#00F6FF",fontSize:24,lineHeight:34,fontWeight:"bold"},itemGap:0},tooltip:{show:!0,trigger:"item",formatter:"{b}：{c}家",backgroundColor:"#043250",padding:[13,14,13,11],textStyle:{fontSize:12,color:"#9ED2D8"}},color:r,textStyle:{color:"#9DD1D7",fontSize:14,fontWeight:"400",lineHeight:14},series:[{name:"经营主体类型统计",type:"pie",radius:["76%","88%"],avoidLabelOverlap:!0,minAngle:15,startAngle:80,label:{show:!1,normal:{show:!1,fontSize:12,position:"outside",lineHeight:16,formatter:["{nameS|{b}}","{valueS|{c}家}"].join("："),rich:{nameS:{color:"#9ED2D8"},valueS:{color:"#00F6FF"}}}},labelLine:{show:!1,normal:{show:!1,length:20,length2:10}},hoverAnimation:!0,selectedMode:"multiple",selectedOffset:2,data:[]},{type:"pie",radius:["69%","70%"],minAngle:15,startAngle:80,animation:!0,labelLine:{show:!1},hoverAnimation:!1,z:3,tooltip:{show:!1},label:{show:!1},selectedMode:"multiple",selectedOffset:4,data:[]}]},c={name:"OperatorsNum",props:{mainBodyInTheSystem:{type:Number,default:0}},data:function(){return{chart:null,chartData:[],totalNum:17958}},mounted:function(){this.initPage(),window.addEventListener("resize",this.resizeChart,!1)},methods:{initPage:function(){this.chart=this._initEcharts(this.eContainerRef,l),this.renderChart()},_initEcharts:function(t,e){var a=this.$echarts.init(t);return a.setOption(e),a},renderChart:function(){this.chartData=[{name:"合作社",value:1054},{name:"家庭农场",value:569},{name:"农业企业",value:316},{name:"大户",value:2690},{name:"散户",value:12606},{name:"村组集体",value:723}].map(function(t,e){return o({},t,{color:r[e]})}),this.chart.setOption({series:[{data:this.chartData},{data:this.chartData}]})},resizeChart:function(){this.chart&&this.chart.resize()}},computed:{eContainerRef:function(){return this.$refs.EContainer}},components:{BoxItem:i.default,countTo:n.default}},h=a("W5g0");var u=function(t){a("NmNl")},d=Object(h.a)(c,function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("box-item",{attrs:{title:"经营主体统计"}},[a("div",{staticClass:"panel-body"},[a("div",{staticClass:"chart-panel"},[a("div",{staticClass:"chart-wrap"},[a("div",{ref:"EContainer",staticClass:"echart-container"}),t._v(" "),a("div",{staticClass:"chart-content"},[a("p",{staticClass:"chart-title"},[t._v("经营主体")]),t._v(" "),a("p",{staticClass:"chart-sub-title"},[t._v(t._s(t.totalNum))]),t._v(" "),a("p",{staticClass:"chart-sub-unit"},[t._v("（家）")])])]),t._v(" "),a("div",{staticClass:"chart-legend-wrap"},[a("ul",{staticClass:"chart-legend"},t._l(t.chartData,function(e,i){return a("li",{key:i,staticClass:"legend-item"},[a("i",{staticClass:"dot",style:{backgroundColor:e.color}}),t._v(" "),a("p",{staticClass:"legend"},[t._v("\n\t\t\t\t\t\t\t"+t._s(e.name)+"："),a("i",{staticClass:"legend-value"},[t._v(t._s(e.value))]),t._v("家\n\t\t\t\t\t\t")])])}),0)])]),t._v(" "),a("div",{staticClass:"bottom-info-wrap"},[a("div",{staticClass:"bottom-info"},[t._v("\n\t\t\t\t入网经营主体数："),a("span",{staticClass:"num"},[t._v(t._s(t.mainBodyInTheSystem))]),a("span",{staticClass:"unit"},[t._v("家")])])])])])},[],!1,u,"data-v-db7ebc08",null);e.default=d.exports},NmNl:function(t,e){}});
//# sourceMappingURL=85.2e7e767adef8871dbf3a.js.map