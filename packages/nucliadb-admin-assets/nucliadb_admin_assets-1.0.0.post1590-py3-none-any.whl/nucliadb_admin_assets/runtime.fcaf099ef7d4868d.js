(()=>{"use strict";var e,v={},m={};function r(e){var n=m[e];if(void 0!==n)return n.exports;var t=m[e]={id:e,loaded:!1,exports:{}};return v[e].call(t.exports,t,t.exports,r),t.loaded=!0,t.exports}r.m=v,e=[],r.O=(n,t,o,u)=>{if(!t){var a=1/0;for(i=0;i<e.length;i++){for(var[t,o,u]=e[i],s=!0,d=0;d<t.length;d++)(!1&u||a>=u)&&Object.keys(r.O).every(b=>r.O[b](t[d]))?t.splice(d--,1):(s=!1,u<a&&(a=u));if(s){e.splice(i--,1);var l=o();void 0!==l&&(n=l)}}return n}u=u||0;for(var i=e.length;i>0&&e[i-1][2]>u;i--)e[i]=e[i-1];e[i]=[t,o,u]},r.n=e=>{var n=e&&e.__esModule?()=>e.default:()=>e;return r.d(n,{a:n}),n},r.d=(e,n)=>{for(var t in n)r.o(n,t)&&!r.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:n[t]})},r.f={},r.e=e=>Promise.all(Object.keys(r.f).reduce((n,t)=>(r.f[t](e,n),n),[])),r.u=e=>e+".752feeb2ae75d8e8.js",r.miniCssF=e=>{},r.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),r.o=(e,n)=>Object.prototype.hasOwnProperty.call(e,n),(()=>{var e={},n="nucliadb-admin:";r.l=(t,o,u,i)=>{if(e[t])e[t].push(o);else{var a,s;if(void 0!==u)for(var d=document.getElementsByTagName("script"),l=0;l<d.length;l++){var f=d[l];if(f.getAttribute("src")==t||f.getAttribute("data-webpack")==n+u){a=f;break}}a||(s=!0,(a=document.createElement("script")).type="module",a.charset="utf-8",a.timeout=120,r.nc&&a.setAttribute("nonce",r.nc),a.setAttribute("data-webpack",n+u),a.src=r.tu(t)),e[t]=[o];var c=(g,b)=>{a.onerror=a.onload=null,clearTimeout(p);var h=e[t];if(delete e[t],a.parentNode&&a.parentNode.removeChild(a),h&&h.forEach(_=>_(b)),g)return g(b)},p=setTimeout(c.bind(null,void 0,{type:"timeout",target:a}),12e4);a.onerror=c.bind(null,a.onerror),a.onload=c.bind(null,a.onload),s&&document.head.appendChild(a)}}})(),r.r=e=>{typeof Symbol<"u"&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{var e;r.tt=()=>(void 0===e&&(e={createScriptURL:n=>n},typeof trustedTypes<"u"&&trustedTypes.createPolicy&&(e=trustedTypes.createPolicy("angular#bundler",e))),e)})(),r.tu=e=>r.tt().createScriptURL(e),r.p="",(()=>{var e={121:0};r.f.j=(o,u)=>{var i=r.o(e,o)?e[o]:void 0;if(0!==i)if(i)u.push(i[2]);else if(121!=o){var a=new Promise((f,c)=>i=e[o]=[f,c]);u.push(i[2]=a);var s=r.p+r.u(o),d=new Error;r.l(s,f=>{if(r.o(e,o)&&(0!==(i=e[o])&&(e[o]=void 0),i)){var c=f&&("load"===f.type?"missing":f.type),p=f&&f.target&&f.target.src;d.message="Loading chunk "+o+" failed.\n("+c+": "+p+")",d.name="ChunkLoadError",d.type=c,d.request=p,i[1](d)}},"chunk-"+o,o)}else e[o]=0},r.O.j=o=>0===e[o];var n=(o,u)=>{var d,l,[i,a,s]=u,f=0;if(i.some(p=>0!==e[p])){for(d in a)r.o(a,d)&&(r.m[d]=a[d]);if(s)var c=s(r)}for(o&&o(u);f<i.length;f++)r.o(e,l=i[f])&&e[l]&&e[l][0](),e[l]=0;return r.O(c)},t=self.webpackChunknucliadb_admin=self.webpackChunknucliadb_admin||[];t.forEach(n.bind(null,0)),t.push=n.bind(null,t.push.bind(t))})()})();