webpackJsonp([1],{"69x4":function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAABiUlEQVQ4jc3UP0hWURjH8Y8lmiAISUMIiSJqSS3V4BKJNDRoQSYoFLgVUdEWKi4NQU0vkmCBuNTQIDi5FJRgoIHg4OBSQUm7mEHZn+Gct15u9+gbNPSDh3vuuc/53nue+3sO/7sqioO2woPS+T24gPM4hkq8wRymsZkFrd289mthVkewgqcYQB324gzG8RbnUl+YBR7FK7ThLhpwCK3Yjyv4jhlc2g1YHRNrcBbD+FjyfBOTOIF1PIovTgKH0IIxPE9tCe+FUlTH3CSwH5+FOu2mhRi9EZwLPI7X2CoDCC9Qi+YUsBafyoTx2zr1KeA6Gv8C2BSvH1LAl4IHO8qA7UMP3sXIBY7jBwqCkXfSMA7K+YGlwCU8RDeeCDXNy7+NUSxjIptQmbm/gQOChU5hCovYxmFcFnp7NcJu4R6+pYBf0IerGIlbK9UW7uMOZtEl2G0wrv0DSKjjhNBanYLPqoQOWcBGzLuOZ8Kp9BgXU8CivmI+Rp5WcTpCTxYndwKWozW0yz8G/41+AsiuStZ1eX0UAAAAAElFTkSuQmCC"},Igo0:function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAB2ElEQVQ4ja3Uy0uUURjH8c9IhkIS5WKQ8tJgJNZC7IK0UYzWbmJa1yLof2jZ/9DSTW2kTduiSCIQ06ToMt2gRjMoCgd1QGWaFuedmXdm3qGB+sHhhef5Pd9z3udc+M9Kwf7sjaTcNC5H34EolscjzOFhY8Hu3E37EkAjuIWphNxwNK7hMa4jFzd0NBRMYrEFrFFTkXeyFXAE99DTBqyinqhmpBGYwiwOgmKRH99bY0olPrwL31AzGzGqwAuYqBb8jgrWVpthOzs8X2Jvj1SqEp2IGFVgtq7oQA/jZ/m6xqePtfj2FsvP6O1l9BQddVuQjQOnm1bS1cX4GQobvHnNr5+sLDM4RGY4qRHTcWB/kkNnJ2PjFLd4scLxExw5mmitMCrAnVYua/nQt3Qf+S/strbGgetNmXKZ9zm+rYd+jp4knWZ5ieJ24tRx4GJdqlTi1Uu2NgOsuzvEB4bIZEIvCxuNwKdx4J26VP5zOBJjp0Mf40r3hR2O737QbVTv8n0sqJzFwWMBWDtn9Tp0OIyaFvAgvsIyrqCAcL5awZpVwNWIUXeXc5jBZrukyDuDt5VA42szj3PCL/xNC5F3Ph5Meg9zOI+LuCTc0X7sYhVPcFfoWbmNif9NfwBCE3iWgBkBAQAAAABJRU5ErkJggg=="},"b+x7":function(t,e){},bkaB:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=r("VCTt"),a=r("VKKs");function i(t){if(Array.isArray(t)){for(var e=0,r=Array(t.length);e<t.length;e++)r[e]=t[e];return r}return Array.from(t)}function o(t){return function(){var e=t.apply(this,arguments);return new Promise(function(t,r){return function n(a,i){try{var o=e[a](i),s=o.value}catch(t){return void r(t)}if(!o.done)return Promise.resolve(s).then(function(t){n("next",t)},function(t){n("throw",t)});t(s)}("next")})}}var s,c=(s=null,function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:500;s&&clearTimeout(s),s=setTimeout(t,e)}),l={data:function(){return{keyword:"",list:[],activeIdx:null,searchLoading:!1,scroll:null,delay:1400}},props:{categoryList:{type:Array,default:function(){return[]}},farmAreaInfo:{type:Object,default:function(){return Object(n.b)()}},gisMapFlag:{type:Boolean,default:function(){return!1}},dataTargetFlag:{type:Number,default:function(){return 1}},clearCompanySelect:{type:Boolean,default:function(){return!1}},openOperatorList:{type:Boolean,default:!0}},watch:{clearCompanySelect:function(t){t&&(this.activeIdx="")},openOperatorList:function(t){Object(a.c)("openoperatorlist",t)}},computed:{showSuffixIcon:function(){return this.keyword},containerWidth:function(){var t=300;return $(window).width()>3e3&&(t=400),this.openoperatorlist?t:0},containerHeight:function(){return this.openoperatorlist?"calc(67.6% - 65px)":0},openoperatorlist:{get:function(){return this.openOperatorList},set:function(t){this.$emit("update:openOperatorList",t)}}},mounted:function(){this.initMoudle()},methods:{initMoudle:function(){var t=this;return o(regeneratorRuntime.mark(function e(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return null===Object(a.b)("openoperatorlist")?(Object(a.c)("openoperatorlist",!0),t.openoperatorlist=!0):t.openoperatorlist=Object(a.b)("openoperatorlist"),t.keyword="",t.scroll&&t.scroll.scrollTo(0,0),t.scroll&&t.scroll.destroy(),e.next=6,t.renderList();case 6:t.$nextTick(function(){setTimeout(function(){t.initListScroll()},500)});case 7:case"end":return e.stop()}},e,t)}))()},renderList:function(){var t=this,e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return o(regeneratorRuntime.mark(function r(){var n;return regeneratorRuntime.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:return t.searchLoading=!0,t.list=[],r.next=4,t.getListData(e,t.dataTargetFlag,t.categoryList);case 4:if(n=r.sent,!t.clearStatus||!e){r.next=7;break}return r.abrupt("return");case 7:n.keyword===e&&(t.list=n.list,t.searchLoading=!1,t.scroll&&t.$nextTick(function(){t.scroll.refresh()}));case 8:case"end":return r.stop()}},r,t)}))()},getListData:function(){var t,e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",r=this,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,a=arguments[2];return new Promise((t=o(regeneratorRuntime.mark(function t(o){var s,c,l,u;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:if(!a.length){t.next=6;break}return t.next=3,r.getSnListByAreaAndCategory(e,a);case 3:s=t.sent,t.next=9;break;case 6:return t.next=8,r.getSnListByAreaAndPage(e);case 8:s=t.sent;case 9:if(!((c=r.formateListData(s.slice(0,300),!0)).length<300&&1===n)){t.next=16;break}return t.next=13,r.getZzListByAreaAndPage(e);case 13:l=t.sent,u=l?r.formateListData(l.slice(0,300-c.length),!1):[],c.push.apply(c,i(u));case 16:o({keyword:e,list:c});case 17:case"end":return t.stop()}},t,r)})),function(e){return t.apply(this,arguments)}))},getSnListByAreaAndPage:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return this.$ajax.post(this.$api.overview.getListByAreaAndPage,{farmAreaId:[this.farmAreaInfo.farmAreaId],farmAreaType:this.farmAreaInfo.farmAreaType,keyword:t,pageNo:1,pageSize:300}).then(function(t){var e=t.data;if(0===e.respCode)return e.obj.list}).catch(function(t){console.log(new Error("神农经营主体列表error"),t)})},getZzListByAreaAndPage:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return this.$ajax.post(this.$api.nongwei.getZzListByAreaAndPage,{farmAreaId:[this.farmAreaInfo.farmAreaId],farmAreaType:this.farmAreaInfo.farmAreaType,keyword:t,pageNo:1,pageSize:300}).then(function(t){var e=t.data;if(0===e.respCode)return e.obj.list}).catch(function(t){console.log(new Error("农委经营主体列表error"),t)})},getSnListByAreaAndCategory:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return this.$ajax.post(this.$api.overview.getListByAreaAndCategory,{businessCategoryStrList:e,farmAreaId:[this.farmAreaInfo.farmAreaId],farmAreaType:this.farmAreaInfo.farmAreaType,keyword:t,pageNo:1,pageSize:300}).then(function(t){var e=t.data;if(0===e.respCode)return e.obj.list}).catch(function(t){console.log(new Error("神农经营主体列表by类目 error"),t)})},formateListData:function(t,e){return e?t.map(function(t){return{id:t.farmId,snname:t.farmName,snfarmId:t.farmId,typeName:t.companyCategoryName||"",isSnFlag:!0,countyId:t.countyId}}):t.map(function(t){return{id:t.companyCode,zzname:t.name,zzcompanyCode:t.companyCode,typeName:t.type||"",isSnFlag:!1,countyId:t.countyId}})},changeListStatus:function(t){var e=this;this.openoperatorlist=t,Object(a.c)("openoperatorlist",this.openoperatorlist),this.$nextTick(function(){setTimeout(function(){e.scroll.refresh()},200)})},toFarmDetailPage:function(t){var e=void 0;e=t.isSnFlag?"/farmdetail/"+t.snfarmId:"/gisfarmdetail/"+t.zzcompanyCode,this.$router.push({path:e})},searchList:function(){var t=this;this.searchLoading=!0,c(function(){t.list=[],t.clearStatus=!1,t.renderList(t.keyword)},this.delay)},showFarmAllPlotfn:function(t,e){var r=this;return o(regeneratorRuntime.mark(function n(){var a,i;return regeneratorRuntime.wrap(function(n){for(;;)switch(n.prev=n.next){case 0:if(r.gisMapFlag){n.next=2;break}return n.abrupt("return");case 2:return r.activeIdx=e,r.$emit("toggleLoading",!0),n.next=6,r.getFarmAllPlots(t,t.isSnFlag);case 6:if(a=n.sent,r.activeIdx===e){n.next=9;break}return n.abrupt("return");case 9:if(a){n.next=11;break}return n.abrupt("return",r.$emit("toggleLoading",!1));case 11:i=t.isSnFlag?t.snname:t.zzname,r.$emit("getFarmAllPlotEv",[a,i,{isSnFlag:t.isSnFlag,countyId:t.countyId}]);case 13:case"end":return n.stop()}},n,r)}))()},getFarmAllPlots:function(t,e){var r=this;return e?new Promise(function(e){r.$ajax.post(r.$api.operators.getFarmAllPoltIds,{farmId:t.snfarmId}).then(function(t){var r=t.status,n=t.data;200===r&&0===n.respCode&&e(n.obj.list),e(!1)})}):new Promise(function(e){r.$ajax.post(r.$api.nongwei.getZzListByCompanyCode,{companyCode:t.zzcompanyCode}).then(function(t){var r=t.status,n=t.data;if(200===r&&0===n.respCode){var a=n.obj.map(function(t){return t.gisPlotId});e(a)}e(!1)})})},initListScroll:function(){this.scroll=Object(n.a)(this.$refs.scroll,{scrollbar:{fade:!0}}),this.scroll&&this.scroll.scrollTo(0,0)},clearInputValue:function(){this.clearStatus=!0,this.keyword="",this.renderList()}},activated:function(){this.scroll&&this.scroll.refresh()}},u=r("W5g0");var p=function(t){r("b+x7")},f=Object(u.a)(l,function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"operators-type-list",class:{toggleAni:t.openoperatorlist},style:{height:t.containerHeight,width:t.containerWidth+"px"}},[n("div",{directives:[{name:"show",rawName:"v-show",value:!t.openoperatorlist,expression:"!openoperatorlist"}],staticClass:"top-title"},[t._v("\n\t\t经营主体列表\n\t\t"),n("div",{staticClass:"expand",on:{click:function(e){return t.changeListStatus(!0)}}})]),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:t.openoperatorlist,expression:"openoperatorlist"}],staticClass:"main"},[n("div",{staticClass:"input-container"},[n("el-input",{attrs:{placeholder:"搜索经营主体"},on:{input:t.searchList},model:{value:t.keyword,callback:function(e){t.keyword=e},expression:"keyword"}},[n("i",{staticClass:"self-icon self-prefix",attrs:{slot:"prefix"},slot:"prefix"},[n("img",{attrs:{src:r("69x4")}})]),t._v(" "),n("i",{directives:[{name:"show",rawName:"v-show",value:t.showSuffixIcon,expression:"showSuffixIcon"}],staticClass:"self-icon self-suffix",attrs:{slot:"suffix"},on:{click:t.clearInputValue},slot:"suffix"},[n("img",{attrs:{src:r("Igo0")}})])])],1),t._v(" "),n("div",{ref:"scroll",staticClass:"list"},[n("ul",{directives:[{name:"show",rawName:"v-show",value:t.list.length,expression:"list.length"}]},t._l(t.list,function(e,r){return n("li",{key:e,class:{active:t.activeIdx===e.id,noGisMap:!t.gisMapFlag},on:{click:function(r){return t.showFarmAllPlotfn(e,e.id)}}},[n("div",{staticClass:"title"},[n("span",{staticClass:"icon",attrs:{title:"数据来源于：种植业管理系统"}},[e.isSnFlag?t._e():n("i",{staticClass:"iconfont icon-lianjie"})]),t._v(" "),n("span",{staticClass:"name"},[t._v(t._s(e.isSnFlag?e.snname:e.zzname))])]),t._v(" "),n("div",{staticClass:"resource-wrapper"},[e.typeName?n("span",[t._v(t._s(e.typeName))]):t._e()]),t._v(" "),n("div",{staticClass:"icon-wrapper"},[t.gisMapFlag?n("span",{staticClass:"dikuai-icon",class:{active:e.id===t.activeIdx},attrs:{title:"查看地块"},on:{click:function(r){return r.stopPropagation(),t.showFarmAllPlotfn(e,e.id)}}}):t._e(),t._v(" "),n("span",{staticClass:"detail-icon",attrs:{title:"进入基地"},on:{click:function(r){return r.stopPropagation(),t.toFarmDetailPage(e)}}})])])}),0),t._v(" "),t.searchLoading?n("div",{directives:[{name:"loading",rawName:"v-loading",value:t.searchLoading,expression:"searchLoading"}],staticClass:"search-loader",attrs:{"element-loading-text":"正在加载...","element-loading-spinner":"el-icon-loading","element-loading-background":"rgba(0, 0, 0, 0)"}}):t._e(),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:0===t.list.length&&!1===t.searchLoading,expression:"list.length === 0 && searchLoading === false"}],staticClass:"no_result"},[n("img",{attrs:{src:r("hfhH"),alt:""}}),t._v(" "),n("div",{staticClass:"text"},[t._v(t._s(t.keyword?"暂无搜索结果":"暂无主体数据"))])])])]),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:t.openoperatorlist,expression:"openoperatorlist"}],staticClass:"close",on:{click:function(e){return t.changeListStatus(!1)}}})])},[],!1,p,"data-v-04f89d0c",null);e.default=f.exports},hfhH:function(t,e){t.exports="https://snkoudai.oss-cn-hangzhou.aliyuncs.com/goverment/static/img/no_result.9f15081.png"}});
//# sourceMappingURL=1.16ce6ec6c640f08b787f.js.map