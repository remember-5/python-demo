webpackJsonp([23],{"7m0v":function(s,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a={data:function(){return{}},props:{missionList:{type:Array,default:function(){return[]}}},created:function(){},methods:{showMissionInputList:function(s){return 1===(s=Number(s))||6===s}},computed:{},filters:{fMissionName:function(s){switch(Number(s)){case 0:return"种植";case 1:return"施肥";case 2:return"灌溉";case 3:return"其他农事";case 4:return"采收";case 5:return"销售";case 6:return"用药";default:return"未知"}}},components:{}},i=e("W5g0");var n=function(s){e("ppSe")},r=Object(i.a)(a,function(){var s=this,t=s.$createElement,a=s._self._c||t;return a("div",[s.missionList.length?a("ul",{staticClass:"farminglist"},s._l(s.missionList,function(t){return a("li",{key:t.id,staticClass:"farmingitem"},[a("div",{staticClass:"line"}),s._v(" "),a("div",{staticClass:"farm-info"},[a("p",{staticClass:"title"},[s._v(s._s(s._f("fMissionName")(t.ftype)))]),s._v(" "),a("p",{staticClass:"info"},[t.subItem.completeTime?a("span",{staticClass:"time"},[s._v(s._s(s._f("znDateFormat")(t.subItem.completeTime,"yyyy.MM.dd")))]):s._e(),s._v(" "),t.subItem.worker||t.subItem.floodingMan?a("span",{staticClass:"person"},[a("img",{attrs:{src:e("SBRL"),alt:"负责人logo"}}),s._v(s._s(t.subItem.worker||t.subItem.floodingMan))]):s._e()]),s._v(" "),s.showMissionInputList(t.ftype)?a("div",{staticClass:"source-list"},[a("div",{staticClass:"source"},[a("p",{staticClass:"description"},[a("span",{staticClass:"name"},[s._v(s._s(t.subItem.name))]),s._v(" "),t.subItem.amount?a("span",{staticClass:"specification"},[s._v(s._s(t.subItem.amount)+" "+s._s("6"===t.ftype?"克/毫升":"公斤"))]):s._e(),s._v(" "),t.subItem.remark||t.subItem.supplyCompany?a("span",{staticClass:"factory"},[s._v("厂家："+s._s("6"===t.ftype?t.subItem.remark:t.subItem.supplyCompany))]):s._e()])])]):s._e()])])}),0):s.missionList.length?s._e():a("div",{staticClass:"nodata"},[a("img",{attrs:{src:e("y8Nw"),alt:"无数据"}}),s._v(" "),a("p",[s._v("暂无农事记录")])])])},[],!1,n,"data-v-b2e18510",null);t.default=r.exports},ppSe:function(s,t){}});
//# sourceMappingURL=23.3e09a5156f1c03dc2fe2.js.map