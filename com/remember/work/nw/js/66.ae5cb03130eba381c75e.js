webpackJsonp([66],{"+BDs":function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAABf0lEQVQ4jb3TQYiNURjG8d93cYlrpcRCYjMxYaGU7G2JLGcrWdqwtrCYja0dJUnN3maSBaVkJRsKGSOykTETMh4L55rv3rn3u3ckb719X+855/8+55zn8I+j+vOX1OstnMZJHMR6vMRd3MCX1aSqr5B0c7/kqSSSn5I3kueS76X2UXKiNr9fTA/wgORTWXxFsrO2qCM5K/kgWZZMjQJulLyQfJMcX6VgJXcV1V8lE03Ac2VLFxtg3TxW5t5qAt6TLEk2jwEkeSBZKDvruc1uHMZjLA1oNyjuo4O99WId2MHimDBWrLNtGHAeu9cA3FO+bwcPJzfLQU+OcX6bJO8kr5ou5Ugx8qxk3Qjg5dL8wihjXysT7xQj94Nakkul8ZOitAfY/5bbuI1TeI/reIQf2IcpHMIzXMV2TGO56S1XkvOS+aK2nouSacnW4ttIZiTtYQrrsQFH/fZZG3N4iM9lfBKz2IEZVXVmmMK15IRkTvJ6HIXjxha0VNXC3wL+b/wCW8SP4yTIK98AAAAASUVORK5CYII="},ckTI:function(t,e){},ydj4:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=a("wx4u");function n(t){return function(){var e=t.apply(this,arguments);return new Promise(function(t,a){return function r(n,o){try{var i=e[n](o),s=i.value}catch(t){return void a(t)}if(!i.done)return Promise.resolve(s).then(function(t){r("next",t)},function(t){r("throw",t)});t(s)}("next")})}}var o={data:function(){return{plantsearch:"",plantPredictDialogShow:!1,cropList:[],searchHasResult:!0,tabindex:!0,cropTypeList:[]}},props:{corpactiveid:{default:"",type:String}},computed:{corpActiveId:{get:function(){return this.corpactiveid},set:function(t){this.$emit("update:corpactiveid",t)}}},watch:{plantsearch:function(t){var e=this;this.searchHasResult=!1,this.cropList.forEach(function(a){-1!==a.cropName.indexOf(t)?(a.nohas=!1,e.searchHasResult=!0):a.nohas=!0}),this.$nextTick(function(){$(e.$refs.plantlist).getNiceScroll().resize()})},tabindex:function(t){var e=this;this.$nextTick(function(){t?($(e.$refs.plantlist).getNiceScroll().show(),$(e.$refs.planttypelist).getNiceScroll().hide()):($(e.$refs.plantlist).getNiceScroll().hide(),1===$(e.$refs.planttypelist).getNiceScroll().length?$(e.$refs.planttypelist).getNiceScroll().show():$(e.$refs.planttypelist).niceScroll({cursorcolor:"rgba(0, 247, 255 ,0.4)",cursorwidth:"3px",cursorborder:"",autohidemode:!0,railpadding:{top:0,right:8,left:0,bottom:0}}))})}},mounted:function(){var t=this;return n(regeneratorRuntime.mark(function e(){var a,r;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.getBreedList();case 2:return 200===(a=e.sent).status&&0===a.data.respCode&&a.data.obj.list&&(t.cropList=a.data.obj.list),t.$nextTick(function(){$(t.$refs.plantlist).niceScroll({cursorcolor:"rgba(0, 247, 255 ,0.4)",cursorwidth:"3px",cursorborder:"",autohidemode:!0,railpadding:{top:0,right:8,left:0,bottom:0}})}),e.next=7,t.getCropTypeList();case 7:200===(r=e.sent).status&&0===r.data.respCode&&r.data.obj&&(t.cropTypeList=r.data.obj.list);case 9:case"end":return e.stop()}},e,t)}))()},methods:{dislogChangeFn:function(t){t||(this.corpActiveId=""),this.plantPredictDialogShow=t,this.$emit("plantPredictDialogChangeEv",t)},showPlantDetailfn:function(t,e){var a=this;return n(regeneratorRuntime.mark(function r(){var n,o,i,s,c;return regeneratorRuntime.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:return a.corpActiveId="crop"+t,r.next=3,a.getCropStatisticsRes(t);case 3:return 200===(n=r.sent).status&&0===n.data.respCode&&n.data.obj&&(o=n.data.obj.cropVO.cropSubjectIdentifier,i="种植","animal"!==o&&"fishery"!==o||(i="养殖"),s={type:"crop",Id:t,name:e,subjectNum:n.data.obj.farmTotal,plotNum:n.data.obj.landTotal,areaNum:n.data.obj.landArce,cropIdentifier:i},a.$emit("getPlantTitleEv",s)),r.next=7,a.getBreedAllPlots(t);case 7:200===(c=r.sent).status&&0===c.data.respCode&&c.data.obj&&a.$emit("getPlantAllPlotEv",[c.data.obj.list,e]);case 9:case"end":return r.stop()}},r,a)}))()},showCropTypeDetailfn:function(t,e){var a=this;return n(regeneratorRuntime.mark(function r(){var n,o,i,s,c;return regeneratorRuntime.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:return a.corpActiveId="croptype"+t,r.next=3,a.getCropTypeStatisticsRes(t);case 3:return 200===(n=r.sent).status&&0===n.data.respCode&&n.data.obj&&(o=n.data.obj.cropSubjectVO.cropSubjectIdentifier||"agri",i="种植","animal"!==o&&"fishery"!==o||(i="养殖"),s={type:"croptype",Id:t,name:e,subjectNum:n.data.obj.farmTotal,plotNum:n.data.obj.landTotal,areaNum:n.data.obj.landArce,cropIdentifier:i},a.$emit("getPlantTitleEv",s)),r.next=7,a.getCropTypeAllPlots(t);case 7:200===(c=r.sent).status&&0===c.data.respCode&&c.data.obj&&a.$emit("getPlantAllPlotEv",[c.data.obj.list,e]);case 9:case"end":return r.stop()}},r,a)}))()},showCropPredictfn:function(t){this.$emit("plantPredictDialogChangeEv",!0),this.corpActiveId=t,this.plantPredictDialogShow=!0},getBreedList:function(){var t=this,e=JSON.parse(localStorage.govGovernmentSubjectVO),a=e.subjectLevel,r=[e.provinceId,e.provinceId,e.cityId,e.countyId];return new Promise(function(n){t.$ajax.post(t.$api.plotlist.getAreaCrop,{farmAreaId:[r[a]],farmAreaType:e.subjectLevel}).then(function(t){n(t)})})},getCropStatisticsRes:function(t){var e=this,a=JSON.parse(localStorage.govGovernmentSubjectVO),r=a.subjectLevel,n=[a.provinceId,a.provinceId,a.cityId,a.countyId];return new Promise(function(o){e.$ajax.post(e.$api.operators.getDataByCrop,{cropId:t,farmAreaId:[n[r]],farmAreaType:a.subjectLevel}).then(function(t){o(t)})})},getCropTypeStatisticsRes:function(t){var e=this,a=JSON.parse(localStorage.govGovernmentSubjectVO),r=a.subjectLevel,n=[a.provinceId,a.provinceId,a.cityId,a.countyId];return new Promise(function(o){e.$ajax.post(e.$api.operators.cropPlotStatistics,{cropCategoryId:t,farmAreaId:[n[r]],farmAreaType:a.subjectLevel}).then(function(t){o(t)})})},getBreedAllPlots:function(t){var e=this,a=JSON.parse(localStorage.govGovernmentSubjectVO),r=a.subjectLevel,n=[a.provinceId,a.provinceId,a.cityId,a.countyId];return new Promise(function(o){e.$ajax.post(e.$api.operators.getCropPoltId,{cropId:t,farmAreaId:[n[r]],farmAreaType:a.subjectLevel}).then(function(t){o(t)})})},getCropTypeList:function(){var t=this,e=JSON.parse(localStorage.govGovernmentSubjectVO),a=e.subjectLevel,r=[e.provinceId,e.provinceId,e.cityId,e.countyId];return new Promise(function(n){t.$ajax.post(t.$api.operators.cropCategorylistByArea,{farmAreaId:[r[a]],farmAreaType:e.subjectLevel}).then(function(t){n(t)})})},getCropTypeAllPlots:function(t){var e=this,a=JSON.parse(localStorage.govGovernmentSubjectVO),r=a.subjectLevel,n=[a.provinceId,a.provinceId,a.cityId,a.countyId];return new Promise(function(o){e.$ajax.post(e.$api.operators.cropCategoryAllGisPlotids,{cropCategoryId:t,farmAreaId:[n[r]],farmAreaType:a.subjectLevel}).then(function(t){o(t)})})}},components:{plantPredictDialog:r.default}},i=[function(){var t=this.$createElement,e=this._self._c||t;return e("span",{staticClass:"search-btn"},[e("img",{attrs:{src:a("+BDs"),alt:""}}),this._v("搜索")])}],s=a("W5g0");var c=function(t){a("ckTI")},l=Object(s.a)(o,function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticClass:"gis-plant-breed tabs-container"},[a("div",{staticClass:"tab-detail"},[a("h3",{staticClass:"title"},[a("span",{class:{active:t.tabindex},on:{click:function(){t.tabindex=!0}}},[t._v("在田品种")]),t._v(" "),a("span",{class:{active:!t.tabindex},on:{click:function(){t.tabindex=!1}}},[t._v("在田统计")])]),t._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:t.tabindex,expression:"tabindex"}],staticClass:"list-detail"},[a("div",{staticClass:"list-search"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.plantsearch,expression:"plantsearch"}],attrs:{type:"text",placeholder:"搜索种养品种"},domProps:{value:t.plantsearch},on:{input:function(e){e.target.composing||(t.plantsearch=e.target.value)}}}),t._v(" "),t._m(0)]),t._v(" "),a("div",{ref:"plantlist",staticClass:"list-items"},[t.cropList&&t.cropList.length>0?a("div",[t._l(t.cropList,function(e,r){return!e.nohas&&t.searchHasResult?a("div",{key:e.cropId,staticClass:"item",class:{active:"crop"+e.cropId===t.corpActiveId}},[a("span",{staticClass:"plant-img",on:{click:function(a){return t.showPlantDetailfn(e.cropId,e.cropName)}}},[a("img",{attrs:{src:t._f("aliimg")(e.cropImgUrl,80,80,!0),alt:""}})]),t._v(" "),a("div",{staticClass:"name",on:{click:function(a){return t.showPlantDetailfn(e.cropId,e.cropName)}}},[a("p",{staticClass:"pyc"},[t._v(t._s(e.cropName))]),t._v(" "),a("p",{staticClass:"pyc"},[t._v(t._s(e.sumPlantAcre||0)+" 亩")])]),t._v(" "),a("span",{staticClass:"go-allplants",attrs:{title:"查看地块"},on:{click:function(a){return t.showPlantDetailfn(e.cropId,e.cropName)}}}),t._v(" "),a("span",{staticClass:"plant-plan",attrs:{title:"预计产量"},on:{click:function(a){return t.showCropPredictfn("crop"+e.cropId)}}})]):t._e()}),t._v(" "),t.searchHasResult?t._e():a("p",{staticClass:"nodata"},[t._v("当前搜索无结果")])],2):a("div",[a("p",{staticClass:"nodata"},[t._v("暂无种养品种")])])])]),t._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!t.tabindex,expression:"!tabindex"}],staticClass:"list-detail"},[a("div",{ref:"planttypelist",staticClass:"list-items list-items-plus"},[t.cropTypeList&&t.cropTypeList.length>0?a("div",t._l(t.cropTypeList,function(e,r){return a("div",{key:e.id,staticClass:"cropSubject-con"},[a("p",{staticClass:"title"},[t._v("\n\t\t\t\t\t\t\t\t"+t._s(e.cropSubjectNickname)+"\n\t\t\t\t\t\t\t\t"),a("span",[t._v("共计"+t._s(e.sumPlantAcres)+"亩")])]),t._v(" "),t._l(e.stasticPlantAcreByCropCategory,function(e,r){return a("div",{key:e.cropCategoryId,staticClass:"item",class:{active:"croptype"+e.cropCategoryId===t.corpActiveId}},[a("span",{staticClass:"plant-img type-img",on:{click:function(a){return t.showCropTypeDetailfn(e.cropCategoryId,e.cropCategoryName)}}},[a("img",{attrs:{src:t._f("aliimg")(e.cropCategoryLogoUrl,80,80,!0),alt:""}})]),t._v(" "),a("div",{staticClass:"name",on:{click:function(a){return t.showCropTypeDetailfn(e.cropCategoryId,e.cropCategoryName)}}},[a("p",{staticClass:"pyc"},[t._v(t._s(e.cropCategoryName))]),t._v(" "),a("p",{staticClass:"pyc"},[t._v(t._s(e.sumPlantAcre||0)+" 亩")])]),t._v(" "),a("span",{staticClass:"go-allplants",attrs:{title:"查看地块"},on:{click:function(a){return t.showCropTypeDetailfn(e.cropCategoryId,e.cropCategoryName)}}}),t._v(" "),a("span",{staticClass:"plant-plan",attrs:{title:"预计产量"},on:{click:function(a){return t.showCropPredictfn("croptype"+e.cropCategoryId)}}})])})],2)}),0):a("div",[a("p",{staticClass:"nodata"},[t._v("暂无作物类型")])])])])])]),t._v(" "),t.plantPredictDialogShow?a("plant-predict-dialog",{attrs:{plantPredictDialog:t.plantPredictDialogShow,id:t.corpActiveId},on:{plantDialogChangeEv:t.dislogChangeFn}}):t._e()],1)},i,!1,c,null,null);e.default=l.exports}});
//# sourceMappingURL=66.ae5cb03130eba381c75e.js.map