webpackJsonp([83],{"7/r/":function(e,t){},P6Oo:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=r("VKKs"),a=r("VCTt"),i=r("hhdC"),o=r("MZv5"),u=r("446f"),s=r("W3V3");var c={name:"fisheries",data:function(){return{farmAreaInfo:{},dataTargetFlag:0}},created:function(){this.farmAreaInfo=Object(a.b)();var e=Object(n.b)("govGovernmentSubjectVO");this.dataTargetFlag=Number(e.dataTargetFlag)},mounted:function(){var e,t=this;return(e=regeneratorRuntime.mark(function e(){var r,n,a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:a=function(){if(-1!=r.$route.path.indexOf("/home/fisheries"))for(var e in console.log("fisheries rezise"),r.$refs){var t=r.$refs[e];t.refreshRender&&t.refreshRender()}},n=function(e,t){var r=null;return function(){var n=this,a=arguments;clearTimeout(r),r=setTimeout(function(){e.apply(n,a)},t)}},r=t,window.resizefn=n(a,200),window.removeEventListener("resize",window.resizefn,!1),window.addEventListener("resize",window.resizefn,!1);case 6:case"end":return e.stop()}},e,t)}),function(){var t=e.apply(this,arguments);return new Promise(function(e,r){return function n(a,i){try{var o=t[a](i),u=o.value}catch(e){return void r(e)}if(!o.done)return Promise.resolve(u).then(function(e){n("next",e)},function(e){n("throw",e)});e(u)}("next")})})()},methods:{},components:{BoxItem:u.default,operatorsDynamic:s.default,arcgismapList:i.default,layoutBox:o.default,businessScaleAnalysis:function(){return r.e(36).then(r.bind(null,"xNr8"))},greenCertification:function(){return r.e(41).then(r.bind(null,"h++q"))},aquaticProductsOutput:function(){return r.e(11).then(r.bind(null,"e82Q"))},aquaculture:function(){return r.e(146).then(r.bind(null,"UX8w"))}}},f=r("W5g0");var l=function(e){r("7/r/")},d=Object(f.a)(c,function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{directives:[{name:"title",rawName:"v-title"}],attrs:{id:"fisheries","data-title":"渔业管理"}},[r("arcgismap-list",{attrs:{showLandType:"yuye","data-target-flag":e.dataTargetFlag,categoryList:[5],"delete-aida-land":!1,deleteGreenLand:!0}}),e._v(" "),r("div",{staticClass:"layout-box-wrapper layout-left"},[r("layout-box",{attrs:{disableBackground:!0}},[r("aquaculture"),e._v(" "),r("div",{staticClass:"operators-dynamic-fisher"},[r("box-item",{attrs:{title:"信息直报","show-sub-title":"","sub-title":"统计"},on:{"hand-sub-title":function(t){return e.$router.push({name:"farmRecordListOther"})}}},[r("operators-dynamic",{attrs:{categoryList:[5],farmAreaInfo:e.farmAreaInfo}})],1)],1)],1)],1),e._v(" "),r("div",{staticClass:"layout-box-wrapper layout-right"},[r("layout-box",{attrs:{disableBackground:!0}},[r("green-certification",{ref:"child3"}),e._v(" "),r("aquatic-productsOutput",{ref:"child4"})],1)],1)],1)},[],!1,l,"data-v-ece5f8b8",null);t.default=d.exports}});
//# sourceMappingURL=83.016ae803f49651ad9684.js.map