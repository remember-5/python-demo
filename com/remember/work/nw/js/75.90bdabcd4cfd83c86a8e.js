webpackJsonp([75],{NQuW:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var i=s("VCTt"),n={props:{farmAreaInfo:{type:Object,default:function(){return Object(i.b)()}},data:{type:Array,default:function(){return[]}},loading:{type:Boolean,default:!1}},data:function(){return{totalBrandCount:0,publicBrandCount:0}},created:function(){},computed:{},mounted:function(){this.getBrandStatics()},methods:{getBrandStatics:function(){var t=this;this.$ajax.post(this.$api.brand.getPpBrandStatics,{farmAreaId:[this.farmAreaInfo.farmAreaId],farmAreaType:this.farmAreaInfo.farmAreaType}).then(function(a){0===a.data.respCode&&(t.totalBrandCount=a.data.obj.totalCount,t.publicBrandCount=a.data.obj.totalSharedCount)})},toBrandList:function(t){this.$router.push({name:"farmProductBrandList",query:{areaId:t}})}},components:{}},e=s("W5g0");var c=function(t){s("VuSM")},o=Object(e.a)(n,function(){var t=this,a=t.$createElement,i=t._self._c||a;return i("div",{staticClass:"statistical"},[i("div",{staticClass:"main"},[i("div",{staticClass:"header"},[i("div",{staticClass:"h-title"},[t._v("\n\t\t\t\t品牌总数"),i("span",[t._v(t._s(t.totalBrandCount))]),t._v("个\n\t\t\t")]),t._v(" "),i("div",{staticClass:"h-title"},[t._v("\n\t\t\t\t公用品牌"),i("span",[t._v(t._s(t.publicBrandCount))]),t._v("个\n\t\t\t")])]),t._v(" "),i("div",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],staticClass:"area-map",attrs:{"element-loading-spinner":"iconfont icon-loading1","element-loading-background":"rgba(0, 0, 0, 0)"}},[i("img",{attrs:{src:s("Oa+a"),alt:""}}),t._v(" "),t._l(t.data,function(a,s){return i("div",{key:a.areaId,staticClass:"statistical-item",class:"statistical-item-"+(s+1)},[i("div",{staticClass:"dot"}),t._v(" "),i("div",{staticClass:"line"}),t._v(" "),i("div",{staticClass:"statistical-item-box",on:{click:function(s){return t.toBrandList(a.areaId)}}},[i("div",{staticClass:"statistical-item-head"},[i("span",{staticClass:"statistical-item-title"},[t._v(t._s(a.name))]),t._v(" "),i("i",{staticClass:"iconfont icon-shang1-copy"})]),t._v(" "),i("div",{staticClass:"statistical-item-body"},[i("div",{staticClass:"statistical-item-desc"},[i("span",{staticClass:"label"},[t._v("品牌总数")]),t._v(" "),i("span",{staticClass:"count"},[t._v(t._s(a.count))])]),t._v(" "),i("div",{staticClass:"statistical-item-desc"},[i("span",{staticClass:"label"},[t._v("公用品牌")]),t._v(" "),i("span",{staticClass:"count"},[t._v(t._s(a.sharedCount))])])])])])})],2)])])},[],!1,c,"data-v-3d914411",null);a.default=o.exports},"Oa+a":function(t,a){t.exports="https://snkoudai.oss-cn-hangzhou.aliyuncs.com/goverment/static/img/shanghai_map.75117eb.png"},VuSM:function(t,a){}});
//# sourceMappingURL=75.90bdabcd4cfd83c86a8e.js.map