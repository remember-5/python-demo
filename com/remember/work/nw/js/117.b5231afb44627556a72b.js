webpackJsonp([117],{CSKJ:function(t,a,e){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var s={name:"SownAreaAndYield",props:{},data:function(){return{totalArea:141.47,areaFloat:null,totalYield:284.7,yieldFloat:null,carouselData:[[{name:"宝山区",area:2.68,cropYield:4.8},{name:"嘉定区",area:9.18,cropYield:12.97},{name:"青浦区",area:16.28,cropYield:40.41}],[{name:"松江区",area:4.68,cropYield:9.51},{name:"金山区",area:17,cropYield:35.75},{name:"闵行区",area:4.9,cropYield:6}],[{name:"奉贤区",area:15.78,cropYield:29.68},{name:"浦东新区",area:22.71,cropYield:47.91},{name:"崇明区",area:41.01,cropYield:79.29}]],carouseActionIndex:0,carouselAutoplay:!0}},created:function(){},mounted:function(){},methods:{nextCarousel:function(){this.carouselElRef.next()},prevCarousel:function(){this.carouselElRef.prev()},carouselChange:function(t){this.carouseActionIndex=t},disabledAutoplay:function(){this.carouselAutoplay=!1},startAutoplay:function(){this.carouselAutoplay=!0}},computed:{carouselElRef:function(){return this.$refs.carouselEl}},components:{BoxItem:e("446f").default}},l=e("W5g0");var o=function(t){e("ICk0")},i=Object(l.a)(s,function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("box-item",{attrs:{title:"播种面积和产量"}},[e("div",{staticClass:"module-wrap"},[e("div",{staticClass:"info-wrap"},[e("ul",{staticClass:"info-ul"},[e("li",{staticClass:"info-item"},[e("p",{staticClass:"info-name"},[t._v("播种面积")]),t._v(" "),e("p",{staticClass:"info-value"},[e("b",{staticClass:"value"},[t._v(t._s(t.totalArea))]),t._v("万亩\n\t\t\t\t\t")]),t._v(" "),t.areaFloat?e("p",{staticClass:"info-juxtapose"},[t._v("\n\t\t\t\t\t\t同比\n\t\t\t\t\t\t"),e("b",{staticClass:"juxtapose-value"},[t._v(" "+t._s(t.areaFloat)+"% "),e("i",{staticClass:"iconfont icon-up"})])]):t._e()]),t._v(" "),e("li",{staticClass:"info-item"},[e("p",{staticClass:"info-name"},[t._v("产量")]),t._v(" "),e("p",{staticClass:"info-value"},[e("b",{staticClass:"value"},[t._v(t._s(t.totalYield))]),t._v("万吨\n\t\t\t\t\t")]),t._v(" "),t.yieldFloat?e("p",{staticClass:"info-juxtapose"},[t._v("\n\t\t\t\t\t\t同比\n\t\t\t\t\t\t"),e("b",{staticClass:"juxtapose-value"},[t._v(" "+t._s(t.yieldFloat)+"% "),e("i",{staticClass:"iconfont icon-up"})])]):t._e()])])]),t._v(" "),e("div",{staticClass:"detail-info-wrap"},[e("i",{staticClass:"iconfont icon-xiangshang left",class:{disabled:0===t.carouseActionIndex},on:{click:t.prevCarousel,mouseover:t.disabledAutoplay,mouseout:t.startAutoplay}}),t._v(" "),e("i",{staticClass:"iconfont icon-fangxiang right",class:{disabled:t.carouseActionIndex===t.carouselData.length-1},on:{click:t.nextCarousel,mouseover:t.disabledAutoplay,mouseout:t.startAutoplay}}),t._v(" "),e("el-carousel",{ref:"carouselEl",attrs:{autoplay:t.carouselAutoplay,arrow:"never","indicator-position":"none",interval:3e3},on:{change:t.carouselChange}},t._l(t.carouselData,function(a,s){return e("el-carousel-item",{key:s},[e("ul",{staticClass:"info-ul"},t._l(a,function(a,s){return e("li",{key:s,staticClass:"info-item"},[e("p",{staticClass:"info-name"},[t._v(t._s(a.name))]),t._v(" "),e("p",{staticClass:"info-value"},[t._v("\n\t\t\t\t\t\t\t\t面积："),e("i",{staticClass:"value"},[t._v(t._s(a.area)+"万亩 ")])]),t._v(" "),e("p",{staticClass:"info-value"},[t._v("\n\t\t\t\t\t\t\t\t产量："),e("i",{staticClass:"value"},[t._v(t._s(a.cropYield)+"万吨 ")])])])}),0)])}),1)],1)])])},[],!1,o,"data-v-4b5ce802",null);a.default=i.exports},ICk0:function(t,a){}});
//# sourceMappingURL=117.b5231afb44627556a72b.js.map