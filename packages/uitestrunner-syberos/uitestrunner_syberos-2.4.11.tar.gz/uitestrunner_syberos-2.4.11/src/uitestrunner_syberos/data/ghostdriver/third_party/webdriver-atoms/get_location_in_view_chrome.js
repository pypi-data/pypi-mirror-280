function(){return function(){var k=this;function aa(a,b){var c=a.split("."),d=k;c[0]in d||!d.execScript||d.execScript("var "+c[0]);for(var e;c.length&&(e=c.shift());)c.length||void 0===b?d[e]?d=d[e]:d=d[e]={}:d[e]=b}
function ba(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}function l(a){return"string"==typeof a}function ca(a,b,c){return a.call.apply(a.bind,arguments)}function da(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function ea(a,b,c){ea=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?ca:da;return ea.apply(null,arguments)}function fa(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
function m(a){var b=n;function c(){}c.prototype=b.prototype;a.G=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.F=function(a,c,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[c].apply(a,g)}};var p;function q(a,b){for(var c=a.length,d=l(a)?a.split(""):a,e=0;e<c;e++)e in d&&b.call(void 0,d[e],e,a)}function r(a,b,c){var d=c;q(a,function(c,f){d=b.call(void 0,d,c,f,a)});return d}function ga(a,b){for(var c=a.length,d=l(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a))return!0;return!1}function ha(a){return Array.prototype.concat.apply(Array.prototype,arguments)}function ia(a,b,c){return 2>=arguments.length?Array.prototype.slice.call(a,b):Array.prototype.slice.call(a,b,c)};function t(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}t.prototype.clone=function(){return new t(this.x,this.y)};t.prototype.toString=function(){return"("+this.x+", "+this.y+")"};t.prototype.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};t.prototype.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};t.prototype.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function u(a,b){this.width=a;this.height=b}u.prototype.clone=function(){return new u(this.width,this.height)};u.prototype.toString=function(){return"("+this.width+" x "+this.height+")"};u.prototype.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};u.prototype.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
u.prototype.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function ja(a,b){if(!a||!b)return!1;if(a.contains&&1==b.nodeType)return a==b||a.contains(b);if("undefined"!=typeof a.compareDocumentPosition)return a==b||!!(a.compareDocumentPosition(b)&16);for(;b&&a!=b;)b=b.parentNode;return b==a}
function ka(a,b){if(a==b)return 0;if(a.compareDocumentPosition)return a.compareDocumentPosition(b)&2?1:-1;if("sourceIndex"in a||a.parentNode&&"sourceIndex"in a.parentNode){var c=1==a.nodeType,d=1==b.nodeType;if(c&&d)return a.sourceIndex-b.sourceIndex;var e=a.parentNode,f=b.parentNode;return e==f?la(a,b):!c&&ja(e,b)?-1*ma(a,b):!d&&ja(f,a)?ma(b,a):(c?a.sourceIndex:e.sourceIndex)-(d?b.sourceIndex:f.sourceIndex)}d=w(a);c=d.createRange();c.selectNode(a);c.collapse(!0);d=d.createRange();d.selectNode(b);
d.collapse(!0);return c.compareBoundaryPoints(k.Range.START_TO_END,d)}function ma(a,b){var c=a.parentNode;if(c==b)return-1;for(var d=b;d.parentNode!=c;)d=d.parentNode;return la(d,a)}function la(a,b){for(var c=b;c=c.previousSibling;)if(c==a)return-1;return 1}function w(a){return 9==a.nodeType?a:a.ownerDocument||a.document}function na(a){this.a=a||k.document||document}
function oa(a){a=a.a;a=(a.parentWindow||a.defaultView||window).document;a="CSS1Compat"==a.compatMode?a.documentElement:a.body;return new u(a.clientWidth,a.clientHeight)};/*

 The MIT License

 Copyright (c) 2007 Cybozu Labs, Inc.
 Copyright (c) 2012 Google Inc.

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to
 deal in the Software without restriction, including without limitation the
 rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 sell copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 IN THE SOFTWARE.
*/
function x(a,b,c){this.a=a;this.b=b||1;this.f=c||1};function pa(a){this.b=a;this.a=0}function qa(a){a=a.match(ra);for(var b=0;b<a.length;b++)sa.test(a[b])&&a.splice(b,1);return new pa(a)}var ra=RegExp("\\$?(?:(?![0-9-\\.])(?:\\*|[\\w-\\.]+):)?(?![0-9-\\.])(?:\\*|[\\w-\\.]+)|\\/\\/|\\.\\.|::|\\d+(?:\\.\\d*)?|\\.\\d+|\"[^\"]*\"|'[^']*'|[!<>]=|\\s+|.","g"),sa=/^\s/;function y(a,b){return a.b[a.a+(b||0)]}function z(a){return a.b[a.a++]}function ta(a){return a.b.length<=a.a};function A(a){var b=null,c=a.nodeType;1==c&&(b=a.textContent,b=void 0==b||null==b?a.innerText:b,b=void 0==b||null==b?"":b);if("string"!=typeof b)if(9==c||1==c){a=9==c?a.documentElement:a.firstChild;for(var c=0,d=[],b="";a;){do 1!=a.nodeType&&(b+=a.nodeValue),d[c++]=a;while(a=a.firstChild);for(;c&&!(a=d[--c].nextSibling););}}else b=a.nodeValue;return""+b}
function C(a,b,c){if(null===b)return!0;try{if(!a.getAttribute)return!1}catch(d){return!1}return null==c?!!a.getAttribute(b):a.getAttribute(b,2)==c}function D(a,b,c,d,e){return ua.call(null,a,b,l(c)?c:null,l(d)?d:null,e||new E)}
function ua(a,b,c,d,e){b.getElementsByName&&d&&"name"==c?(b=b.getElementsByName(d),q(b,function(b){a.a(b)&&F(e,b)})):b.getElementsByClassName&&d&&"class"==c?(b=b.getElementsByClassName(d),q(b,function(b){b.className==d&&a.a(b)&&F(e,b)})):a instanceof G?va(a,b,c,d,e):b.getElementsByTagName&&(b=b.getElementsByTagName(a.f()),q(b,function(a){C(a,c,d)&&F(e,a)}));return e}function wa(a,b,c,d,e){for(b=b.firstChild;b;b=b.nextSibling)C(b,c,d)&&a.a(b)&&F(e,b);return e}
function va(a,b,c,d,e){for(b=b.firstChild;b;b=b.nextSibling)C(b,c,d)&&a.a(b)&&F(e,b),va(a,b,c,d,e)};function E(){this.b=this.a=null;this.l=0}function xa(a){this.node=a;this.a=this.b=null}function ya(a,b){if(!a.a)return b;if(!b.a)return a;for(var c=a.a,d=b.a,e=null,f=null,g=0;c&&d;)c.node==d.node?(f=c,c=c.a,d=d.a):0<ka(c.node,d.node)?(f=d,d=d.a):(f=c,c=c.a),(f.b=e)?e.a=f:a.a=f,e=f,g++;for(f=c||d;f;)f.b=e,e=e.a=f,g++,f=f.a;a.b=e;a.l=g;return a}E.prototype.unshift=function(a){a=new xa(a);a.a=this.a;this.b?this.a.b=a:this.a=this.b=a;this.a=a;this.l++};
function F(a,b){var c=new xa(b);c.b=a.b;a.a?a.b.a=c:a.a=a.b=c;a.b=c;a.l++}function za(a){return(a=a.a)?a.node:null}function Aa(a){return(a=za(a))?A(a):""}function H(a,b){return new Ba(a,!!b)}function Ba(a,b){this.f=a;this.b=(this.c=b)?a.b:a.a;this.a=null}function I(a){var b=a.b;if(null==b)return null;var c=a.a=b;a.b=a.c?b.b:b.a;return c.node};function n(a){this.i=a;this.b=this.g=!1;this.f=null}function J(a){return"\n  "+a.toString().split("\n").join("\n  ")}function Ca(a,b){a.g=b}function Da(a,b){a.b=b}function K(a,b){var c=a.a(b);return c instanceof E?+Aa(c):+c}function L(a,b){var c=a.a(b);return c instanceof E?Aa(c):""+c}function M(a,b){var c=a.a(b);return c instanceof E?!!c.l:!!c};function N(a,b,c){n.call(this,a.i);this.c=a;this.h=b;this.o=c;this.g=b.g||c.g;this.b=b.b||c.b;this.c==Ea&&(c.b||c.g||4==c.i||0==c.i||!b.f?b.b||b.g||4==b.i||0==b.i||!c.f||(this.f={name:c.f.name,s:b}):this.f={name:b.f.name,s:c})}m(N);
function O(a,b,c,d,e){b=b.a(d);c=c.a(d);var f;if(b instanceof E&&c instanceof E){b=H(b);for(d=I(b);d;d=I(b))for(e=H(c),f=I(e);f;f=I(e))if(a(A(d),A(f)))return!0;return!1}if(b instanceof E||c instanceof E){b instanceof E?(e=b,d=c):(e=c,d=b);f=H(e);for(var g=typeof d,h=I(f);h;h=I(f)){switch(g){case "number":h=+A(h);break;case "boolean":h=!!A(h);break;case "string":h=A(h);break;default:throw Error("Illegal primitive type for comparison.");}if(e==b&&a(h,d)||e==c&&a(d,h))return!0}return!1}return e?"boolean"==
typeof b||"boolean"==typeof c?a(!!b,!!c):"number"==typeof b||"number"==typeof c?a(+b,+c):a(b,c):a(+b,+c)}N.prototype.a=function(a){return this.c.m(this.h,this.o,a)};N.prototype.toString=function(){var a="Binary Expression: "+this.c,a=a+J(this.h);return a+=J(this.o)};function Fa(a,b,c,d){this.a=a;this.w=b;this.i=c;this.m=d}Fa.prototype.toString=function(){return this.a};var Ga={};
function P(a,b,c,d){if(Ga.hasOwnProperty(a))throw Error("Binary operator already created: "+a);a=new Fa(a,b,c,d);return Ga[a.toString()]=a}P("div",6,1,function(a,b,c){return K(a,c)/K(b,c)});P("mod",6,1,function(a,b,c){return K(a,c)%K(b,c)});P("*",6,1,function(a,b,c){return K(a,c)*K(b,c)});P("+",5,1,function(a,b,c){return K(a,c)+K(b,c)});P("-",5,1,function(a,b,c){return K(a,c)-K(b,c)});P("<",4,2,function(a,b,c){return O(function(a,b){return a<b},a,b,c)});
P(">",4,2,function(a,b,c){return O(function(a,b){return a>b},a,b,c)});P("<=",4,2,function(a,b,c){return O(function(a,b){return a<=b},a,b,c)});P(">=",4,2,function(a,b,c){return O(function(a,b){return a>=b},a,b,c)});var Ea=P("=",3,2,function(a,b,c){return O(function(a,b){return a==b},a,b,c,!0)});P("!=",3,2,function(a,b,c){return O(function(a,b){return a!=b},a,b,c,!0)});P("and",2,2,function(a,b,c){return M(a,c)&&M(b,c)});P("or",1,2,function(a,b,c){return M(a,c)||M(b,c)});function Ha(a,b){if(b.a.length&&4!=a.i)throw Error("Primary expression must evaluate to nodeset if filter has predicate(s).");n.call(this,a.i);this.c=a;this.h=b;this.g=a.g;this.b=a.b}m(Ha);Ha.prototype.a=function(a){a=this.c.a(a);return Ia(this.h,a)};Ha.prototype.toString=function(){var a;a="Filter:"+J(this.c);return a+=J(this.h)};function Ja(a,b){if(b.length<a.A)throw Error("Function "+a.j+" expects at least"+a.A+" arguments, "+b.length+" given");if(null!==a.v&&b.length>a.v)throw Error("Function "+a.j+" expects at most "+a.v+" arguments, "+b.length+" given");a.B&&q(b,function(b,d){if(4!=b.i)throw Error("Argument "+d+" to function "+a.j+" is not of type Nodeset: "+b);});n.call(this,a.i);this.h=a;this.c=b;Ca(this,a.g||ga(b,function(a){return a.g}));Da(this,a.D&&!b.length||a.C&&!!b.length||ga(b,function(a){return a.b}))}m(Ja);
Ja.prototype.a=function(a){return this.h.m.apply(null,ha(a,this.c))};Ja.prototype.toString=function(){var a="Function: "+this.h;if(this.c.length)var b=r(this.c,function(a,b){return a+J(b)},"Arguments:"),a=a+J(b);return a};function Ka(a,b,c,d,e,f,g,h,v){this.j=a;this.i=b;this.g=c;this.D=d;this.C=e;this.m=f;this.A=g;this.v=void 0!==h?h:g;this.B=!!v}Ka.prototype.toString=function(){return this.j};var La={};
function Q(a,b,c,d,e,f,g,h){if(La.hasOwnProperty(a))throw Error("Function already created: "+a+".");La[a]=new Ka(a,b,c,d,!1,e,f,g,h)}Q("boolean",2,!1,!1,function(a,b){return M(b,a)},1);Q("ceiling",1,!1,!1,function(a,b){return Math.ceil(K(b,a))},1);Q("concat",3,!1,!1,function(a,b){return r(ia(arguments,1),function(b,d){return b+L(d,a)},"")},2,null);Q("contains",2,!1,!1,function(a,b,c){b=L(b,a);a=L(c,a);return-1!=b.indexOf(a)},2);Q("count",1,!1,!1,function(a,b){return b.a(a).l},1,1,!0);
Q("false",2,!1,!1,function(){return!1},0);Q("floor",1,!1,!1,function(a,b){return Math.floor(K(b,a))},1);Q("id",4,!1,!1,function(a,b){var c=a.a,d=9==c.nodeType?c:c.ownerDocument,c=L(b,a).split(/\s+/),e=[];q(c,function(a){a=d.getElementById(a);var b;if(!(b=!a)){a:if(l(e))b=l(a)&&1==a.length?e.indexOf(a,0):-1;else{for(b=0;b<e.length;b++)if(b in e&&e[b]===a)break a;b=-1}b=0<=b}b||e.push(a)});e.sort(ka);var f=new E;q(e,function(a){F(f,a)});return f},1);Q("lang",2,!1,!1,function(){return!1},1);
Q("last",1,!0,!1,function(a){if(1!=arguments.length)throw Error("Function last expects ()");return a.f},0);Q("local-name",3,!1,!0,function(a,b){var c=b?za(b.a(a)):a.a;return c?c.localName||c.nodeName.toLowerCase():""},0,1,!0);Q("name",3,!1,!0,function(a,b){var c=b?za(b.a(a)):a.a;return c?c.nodeName.toLowerCase():""},0,1,!0);Q("namespace-uri",3,!0,!1,function(){return""},0,1,!0);
Q("normalize-space",3,!1,!0,function(a,b){return(b?L(b,a):A(a.a)).replace(/[\s\xa0]+/g," ").replace(/^\s+|\s+$/g,"")},0,1);Q("not",2,!1,!1,function(a,b){return!M(b,a)},1);Q("number",1,!1,!0,function(a,b){return b?K(b,a):+A(a.a)},0,1);Q("position",1,!0,!1,function(a){return a.b},0);Q("round",1,!1,!1,function(a,b){return Math.round(K(b,a))},1);Q("starts-with",2,!1,!1,function(a,b,c){b=L(b,a);a=L(c,a);return 0==b.lastIndexOf(a,0)},2);Q("string",3,!1,!0,function(a,b){return b?L(b,a):A(a.a)},0,1);
Q("string-length",1,!1,!0,function(a,b){return(b?L(b,a):A(a.a)).length},0,1);Q("substring",3,!1,!1,function(a,b,c,d){c=K(c,a);if(isNaN(c)||Infinity==c||-Infinity==c)return"";d=d?K(d,a):Infinity;if(isNaN(d)||-Infinity===d)return"";c=Math.round(c)-1;var e=Math.max(c,0);a=L(b,a);return Infinity==d?a.substring(e):a.substring(e,c+Math.round(d))},2,3);Q("substring-after",3,!1,!1,function(a,b,c){b=L(b,a);a=L(c,a);c=b.indexOf(a);return-1==c?"":b.substring(c+a.length)},2);
Q("substring-before",3,!1,!1,function(a,b,c){b=L(b,a);a=L(c,a);a=b.indexOf(a);return-1==a?"":b.substring(0,a)},2);Q("sum",1,!1,!1,function(a,b){for(var c=H(b.a(a)),d=0,e=I(c);e;e=I(c))d+=+A(e);return d},1,1,!0);Q("translate",3,!1,!1,function(a,b,c,d){b=L(b,a);c=L(c,a);var e=L(d,a);a={};for(d=0;d<c.length;d++){var f=c.charAt(d);f in a||(a[f]=e.charAt(d))}c="";for(d=0;d<b.length;d++)f=b.charAt(d),c+=f in a?a[f]:f;return c},3);Q("true",2,!1,!1,function(){return!0},0);function G(a,b){this.h=a;this.c=void 0!==b?b:null;this.b=null;switch(a){case "comment":this.b=8;break;case "text":this.b=3;break;case "processing-instruction":this.b=7;break;case "node":break;default:throw Error("Unexpected argument");}}function Ma(a){return"comment"==a||"text"==a||"processing-instruction"==a||"node"==a}G.prototype.a=function(a){return null===this.b||this.b==a.nodeType};G.prototype.f=function(){return this.h};
G.prototype.toString=function(){var a="Kind Test: "+this.h;null===this.c||(a+=J(this.c));return a};function Na(a){n.call(this,3);this.c=a.substring(1,a.length-1)}m(Na);Na.prototype.a=function(){return this.c};Na.prototype.toString=function(){return"Literal: "+this.c};function R(a,b){this.j=a.toLowerCase();var c;c="*"==this.j?"*":"http://www.w3.org/1999/xhtml";this.b=b?b.toLowerCase():c}R.prototype.a=function(a){var b=a.nodeType;return 1!=b&&2!=b?!1:"*"!=this.j&&this.j!=a.localName.toLowerCase()?!1:"*"==this.b?!0:this.b==(a.namespaceURI?a.namespaceURI.toLowerCase():"http://www.w3.org/1999/xhtml")};R.prototype.f=function(){return this.j};R.prototype.toString=function(){return"Name Test: "+("http://www.w3.org/1999/xhtml"==this.b?"":this.b+":")+this.j};function Oa(a){n.call(this,1);this.c=a}m(Oa);Oa.prototype.a=function(){return this.c};Oa.prototype.toString=function(){return"Number: "+this.c};function Pa(a,b){n.call(this,a.i);this.h=a;this.c=b;this.g=a.g;this.b=a.b;if(1==this.c.length){var c=this.c[0];c.u||c.c!=Qa||(c=c.o,"*"!=c.f()&&(this.f={name:c.f(),s:null}))}}m(Pa);function S(){n.call(this,4)}m(S);S.prototype.a=function(a){var b=new E;a=a.a;9==a.nodeType?F(b,a):F(b,a.ownerDocument);return b};S.prototype.toString=function(){return"Root Helper Expression"};function Ra(){n.call(this,4)}m(Ra);Ra.prototype.a=function(a){var b=new E;F(b,a.a);return b};Ra.prototype.toString=function(){return"Context Helper Expression"};
function Sa(a){return"/"==a||"//"==a}Pa.prototype.a=function(a){var b=this.h.a(a);if(!(b instanceof E))throw Error("Filter expression must evaluate to nodeset.");a=this.c;for(var c=0,d=a.length;c<d&&b.l;c++){var e=a[c],f=H(b,e.c.a),g;if(e.g||e.c!=Ta)if(e.g||e.c!=Ua)for(g=I(f),b=e.a(new x(g));null!=(g=I(f));)g=e.a(new x(g)),b=ya(b,g);else g=I(f),b=e.a(new x(g));else{for(g=I(f);(b=I(f))&&(!g.contains||g.contains(b))&&b.compareDocumentPosition(g)&8;g=b);b=e.a(new x(g))}}return b};
Pa.prototype.toString=function(){var a;a="Path Expression:"+J(this.h);if(this.c.length){var b=r(this.c,function(a,b){return a+J(b)},"Steps:");a+=J(b)}return a};function Va(a,b){this.a=a;this.b=!!b}
function Ia(a,b,c){for(c=c||0;c<a.a.length;c++)for(var d=a.a[c],e=H(b),f=b.l,g,h=0;g=I(e);h++){var v=a.b?f-h:h+1;g=d.a(new x(g,v,f));if("number"==typeof g)v=v==g;else if("string"==typeof g||"boolean"==typeof g)v=!!g;else if(g instanceof E)v=0<g.l;else throw Error("Predicate.evaluate returned an unexpected type.");if(!v){v=e;g=v.f;var B=v.a;if(!B)throw Error("Next must be called at least once before remove.");var T=B.b,B=B.a;T?T.a=B:g.a=B;B?B.b=T:g.b=T;g.l--;v.a=null}}return b}
Va.prototype.toString=function(){return r(this.a,function(a,b){return a+J(b)},"Predicates:")};function U(a,b,c,d){n.call(this,4);this.c=a;this.o=b;this.h=c||new Va([]);this.u=!!d;b=this.h;b=0<b.a.length?b.a[0].f:null;a.b&&b&&(this.f={name:b.name,s:b.s});a:{a=this.h;for(b=0;b<a.a.length;b++)if(c=a.a[b],c.g||1==c.i||0==c.i){a=!0;break a}a=!1}this.g=a}m(U);
U.prototype.a=function(a){var b=a.a,c=null,c=this.f,d=null,e=null,f=0;c&&(d=c.name,e=c.s?L(c.s,a):null,f=1);if(this.u)if(this.g||this.c!=Wa)if(a=H((new U(Xa,new G("node"))).a(a)),b=I(a))for(c=this.m(b,d,e,f);null!=(b=I(a));)c=ya(c,this.m(b,d,e,f));else c=new E;else c=D(this.o,b,d,e),c=Ia(this.h,c,f);else c=this.m(a.a,d,e,f);return c};U.prototype.m=function(a,b,c,d){a=this.c.f(this.o,a,b,c);return a=Ia(this.h,a,d)};
U.prototype.toString=function(){var a;a="Step:"+J("Operator: "+(this.u?"//":"/"));this.c.j&&(a+=J("Axis: "+this.c));a+=J(this.o);if(this.h.a.length){var b=r(this.h.a,function(a,b){return a+J(b)},"Predicates:");a+=J(b)}return a};function Ya(a,b,c,d){this.j=a;this.f=b;this.a=c;this.b=d}Ya.prototype.toString=function(){return this.j};var Za={};function V(a,b,c,d){if(Za.hasOwnProperty(a))throw Error("Axis already created: "+a);b=new Ya(a,b,c,!!d);return Za[a]=b}
V("ancestor",function(a,b){for(var c=new E,d=b;d=d.parentNode;)a.a(d)&&c.unshift(d);return c},!0);V("ancestor-or-self",function(a,b){var c=new E,d=b;do a.a(d)&&c.unshift(d);while(d=d.parentNode);return c},!0);var Qa=V("attribute",function(a,b){var c=new E,d=a.f(),e=b.attributes;if(e)if(a instanceof G&&null===a.b||"*"==d)for(var d=0,f;f=e[d];d++)F(c,f);else(f=e.getNamedItem(d))&&F(c,f);return c},!1),Wa=V("child",function(a,b,c,d,e){return wa.call(null,a,b,l(c)?c:null,l(d)?d:null,e||new E)},!1,!0);
V("descendant",D,!1,!0);var Xa=V("descendant-or-self",function(a,b,c,d){var e=new E;C(b,c,d)&&a.a(b)&&F(e,b);return D(a,b,c,d,e)},!1,!0),Ta=V("following",function(a,b,c,d){var e=new E;do for(var f=b;f=f.nextSibling;)C(f,c,d)&&a.a(f)&&F(e,f),e=D(a,f,c,d,e);while(b=b.parentNode);return e},!1,!0);V("following-sibling",function(a,b){for(var c=new E,d=b;d=d.nextSibling;)a.a(d)&&F(c,d);return c},!1);V("namespace",function(){return new E},!1);
var $a=V("parent",function(a,b){var c=new E;if(9==b.nodeType)return c;if(2==b.nodeType)return F(c,b.ownerElement),c;var d=b.parentNode;a.a(d)&&F(c,d);return c},!1),Ua=V("preceding",function(a,b,c,d){var e=new E,f=[];do f.unshift(b);while(b=b.parentNode);for(var g=1,h=f.length;g<h;g++){var v=[];for(b=f[g];b=b.previousSibling;)v.unshift(b);for(var B=0,T=v.length;B<T;B++)b=v[B],C(b,c,d)&&a.a(b)&&F(e,b),e=D(a,b,c,d,e)}return e},!0,!0);
V("preceding-sibling",function(a,b){for(var c=new E,d=b;d=d.previousSibling;)a.a(d)&&c.unshift(d);return c},!0);var ab=V("self",function(a,b){var c=new E;a.a(b)&&F(c,b);return c},!1);function bb(a){n.call(this,1);this.c=a;this.g=a.g;this.b=a.b}m(bb);bb.prototype.a=function(a){return-K(this.c,a)};bb.prototype.toString=function(){return"Unary Expression: -"+J(this.c)};function cb(a){n.call(this,4);this.c=a;Ca(this,ga(this.c,function(a){return a.g}));Da(this,ga(this.c,function(a){return a.b}))}m(cb);cb.prototype.a=function(a){var b=new E;q(this.c,function(c){c=c.a(a);if(!(c instanceof E))throw Error("Path expression must evaluate to NodeSet.");b=ya(b,c)});return b};cb.prototype.toString=function(){return r(this.c,function(a,b){return a+J(b)},"Union Expression:")};function db(a,b){this.a=a;this.b=b}function eb(a){for(var b,c=[];;){W(a,"Missing right hand side of binary expression.");b=fb(a);var d=z(a.a);if(!d)break;var e=(d=Ga[d]||null)&&d.w;if(!e){a.a.a--;break}for(;c.length&&e<=c[c.length-1].w;)b=new N(c.pop(),c.pop(),b);c.push(b,d)}for(;c.length;)b=new N(c.pop(),c.pop(),b);return b}function W(a,b){if(ta(a.a))throw Error(b);}function gb(a,b){var c=z(a.a);if(c!=b)throw Error("Bad token, expected: "+b+" got: "+c);}
function hb(a){a=z(a.a);if(")"!=a)throw Error("Bad token: "+a);}function ib(a){a=z(a.a);if(2>a.length)throw Error("Unclosed literal string");return new Na(a)}
function jb(a){var b,c=[],d;if(Sa(y(a.a))){b=z(a.a);d=y(a.a);if("/"==b&&(ta(a.a)||"."!=d&&".."!=d&&"@"!=d&&"*"!=d&&!/(?![0-9])[\w]/.test(d)))return new S;d=new S;W(a,"Missing next location step.");b=kb(a,b);c.push(b)}else{a:{b=y(a.a);d=b.charAt(0);switch(d){case "$":throw Error("Variable reference not allowed in HTML XPath");case "(":z(a.a);b=eb(a);W(a,'unclosed "("');gb(a,")");break;case '"':case "'":b=ib(a);break;default:if(isNaN(+b))if(!Ma(b)&&/(?![0-9])[\w]/.test(d)&&"("==y(a.a,1)){b=z(a.a);b=
La[b]||null;z(a.a);for(d=[];")"!=y(a.a);){W(a,"Missing function argument list.");d.push(eb(a));if(","!=y(a.a))break;z(a.a)}W(a,"Unclosed function argument list.");hb(a);b=new Ja(b,d)}else{b=null;break a}else b=new Oa(+z(a.a))}"["==y(a.a)&&(d=new Va(lb(a)),b=new Ha(b,d))}if(b)if(Sa(y(a.a)))d=b;else return b;else b=kb(a,"/"),d=new Ra,c.push(b)}for(;Sa(y(a.a));)b=z(a.a),W(a,"Missing next location step."),b=kb(a,b),c.push(b);return new Pa(d,c)}
function kb(a,b){var c,d,e;if("/"!=b&&"//"!=b)throw Error('Step op should be "/" or "//"');if("."==y(a.a))return d=new U(ab,new G("node")),z(a.a),d;if(".."==y(a.a))return d=new U($a,new G("node")),z(a.a),d;var f;if("@"==y(a.a))f=Qa,z(a.a),W(a,"Missing attribute name");else if("::"==y(a.a,1)){if(!/(?![0-9])[\w]/.test(y(a.a).charAt(0)))throw Error("Bad token: "+z(a.a));c=z(a.a);f=Za[c]||null;if(!f)throw Error("No axis with name: "+c);z(a.a);W(a,"Missing node name")}else f=Wa;c=y(a.a);if(/(?![0-9])[\w\*]/.test(c.charAt(0)))if("("==
y(a.a,1)){if(!Ma(c))throw Error("Invalid node type: "+c);c=z(a.a);if(!Ma(c))throw Error("Invalid type name: "+c);gb(a,"(");W(a,"Bad nodetype");e=y(a.a).charAt(0);var g=null;if('"'==e||"'"==e)g=ib(a);W(a,"Bad nodetype");hb(a);c=new G(c,g)}else if(c=z(a.a),e=c.indexOf(":"),-1==e)c=new R(c);else{var g=c.substring(0,e),h;if("*"==g)h="*";else if(h=a.b(g),!h)throw Error("Namespace prefix not declared: "+g);c=c.substr(e+1);c=new R(c,h)}else throw Error("Bad token: "+z(a.a));e=new Va(lb(a),f.a);return d||
new U(f,c,e,"//"==b)}function lb(a){for(var b=[];"["==y(a.a);){z(a.a);W(a,"Missing predicate expression.");var c=eb(a);b.push(c);W(a,"Unclosed predicate expression.");gb(a,"]")}return b}function fb(a){if("-"==y(a.a))return z(a.a),new bb(fb(a));var b=jb(a);if("|"!=y(a.a))a=b;else{for(b=[b];"|"==z(a.a);)W(a,"Missing next union location path."),b.push(jb(a));a.a.a--;a=new cb(b)}return a};function mb(a){switch(a.nodeType){case 1:return fa(nb,a);case 9:return mb(a.documentElement);case 11:case 10:case 6:case 12:return ob;default:return a.parentNode?mb(a.parentNode):ob}}function ob(){return null}function nb(a,b){if(a.prefix==b)return a.namespaceURI||"http://www.w3.org/1999/xhtml";var c=a.getAttributeNode("xmlns:"+b);return c&&c.specified?c.value||null:a.parentNode&&9!=a.parentNode.nodeType?nb(a.parentNode,b):null};function pb(a,b){if(!a.length)throw Error("Empty XPath expression.");var c=qa(a);if(ta(c))throw Error("Invalid XPath expression.");b?"function"==ba(b)||(b=ea(b.lookupNamespaceURI,b)):b=function(){return null};var d=eb(new db(c,b));if(!ta(c))throw Error("Bad token: "+z(c));this.evaluate=function(a,b){var c=d.a(new x(a));return new X(c,b)}}
function X(a,b){if(0==b)if(a instanceof E)b=4;else if("string"==typeof a)b=2;else if("number"==typeof a)b=1;else if("boolean"==typeof a)b=3;else throw Error("Unexpected evaluation result.");if(2!=b&&1!=b&&3!=b&&!(a instanceof E))throw Error("value could not be converted to the specified type");this.resultType=b;var c;switch(b){case 2:this.stringValue=a instanceof E?Aa(a):""+a;break;case 1:this.numberValue=a instanceof E?+Aa(a):+a;break;case 3:this.booleanValue=a instanceof E?0<a.l:!!a;break;case 4:case 5:case 6:case 7:var d=
H(a);c=[];for(var e=I(d);e;e=I(d))c.push(e);this.snapshotLength=a.l;this.invalidIteratorState=!1;break;case 8:case 9:this.singleNodeValue=za(a);break;default:throw Error("Unknown XPathResult type.");}var f=0;this.iterateNext=function(){if(4!=b&&5!=b)throw Error("iterateNext called with wrong result type");return f>=c.length?null:c[f++]};this.snapshotItem=function(a){if(6!=b&&7!=b)throw Error("snapshotItem called with wrong result type");return a>=c.length||0>a?null:c[a]}}X.ANY_TYPE=0;
X.NUMBER_TYPE=1;X.STRING_TYPE=2;X.BOOLEAN_TYPE=3;X.UNORDERED_NODE_ITERATOR_TYPE=4;X.ORDERED_NODE_ITERATOR_TYPE=5;X.UNORDERED_NODE_SNAPSHOT_TYPE=6;X.ORDERED_NODE_SNAPSHOT_TYPE=7;X.ANY_UNORDERED_NODE_TYPE=8;X.FIRST_ORDERED_NODE_TYPE=9;function qb(a){this.lookupNamespaceURI=mb(a)}
aa("wgxpath.install",function(a,b){var c=a||k,d=c.document;if(!d.evaluate||b)c.XPathResult=X,d.evaluate=function(a,b,c,d){return(new pb(a,c)).evaluate(b,d)},d.createExpression=function(a,b){return new pb(a,b)},d.createNSResolver=function(a){return new qb(a)}});function Y(a,b,c,d){this.top=a;this.right=b;this.bottom=c;this.left=d}Y.prototype.clone=function(){return new Y(this.top,this.right,this.bottom,this.left)};Y.prototype.toString=function(){return"("+this.top+"t, "+this.right+"r, "+this.bottom+"b, "+this.left+"l)"};Y.prototype.ceil=function(){this.top=Math.ceil(this.top);this.right=Math.ceil(this.right);this.bottom=Math.ceil(this.bottom);this.left=Math.ceil(this.left);return this};
Y.prototype.floor=function(){this.top=Math.floor(this.top);this.right=Math.floor(this.right);this.bottom=Math.floor(this.bottom);this.left=Math.floor(this.left);return this};Y.prototype.round=function(){this.top=Math.round(this.top);this.right=Math.round(this.right);this.bottom=Math.round(this.bottom);this.left=Math.round(this.left);return this};function Z(a,b,c,d){this.left=a;this.top=b;this.width=c;this.height=d}Z.prototype.clone=function(){return new Z(this.left,this.top,this.width,this.height)};Z.prototype.toString=function(){return"("+this.left+", "+this.top+" - "+this.width+"w x "+this.height+"h)"};Z.prototype.ceil=function(){this.left=Math.ceil(this.left);this.top=Math.ceil(this.top);this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
Z.prototype.floor=function(){this.left=Math.floor(this.left);this.top=Math.floor(this.top);this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};Z.prototype.round=function(){this.left=Math.round(this.left);this.top=Math.round(this.top);this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function rb(a,b){var c=w(a);return c.defaultView&&c.defaultView.getComputedStyle&&(c=c.defaultView.getComputedStyle(a,null))?c[b]||c.getPropertyValue(b)||"":""}function sb(a){var b;try{b=a.getBoundingClientRect()}catch(c){return{left:0,top:0,right:0,bottom:0}}return b}
function tb(a){var b=w(a),c=new t(0,0);if(a==(b?w(b):document).documentElement)return c;a=sb(a);var d=(b?new na(w(b)):p||(p=new na)).a,b=d.scrollingElement?d.scrollingElement:d.body||d.documentElement,d=d.parentWindow||d.defaultView,b=new t(d.pageXOffset||b.scrollLeft,d.pageYOffset||b.scrollTop);c.x=a.left+b.x;c.y=a.top+b.y;return c}function ub(a){if(1==a.nodeType)return a=sb(a),new t(a.left,a.top);a=a.changedTouches?a.changedTouches[0]:a;return new t(a.clientX,a.clientY)};var vb="function"===typeof ShadowRoot;function wb(a,b){var c;c=tb(b);var d=tb(a);c=new t(c.x-d.x,c.y-d.y);var e,f,g;g=rb(a,"borderLeftWidth");f=rb(a,"borderRightWidth");e=rb(a,"borderTopWidth");d=rb(a,"borderBottomWidth");d=new Y(parseFloat(e),parseFloat(f),parseFloat(d),parseFloat(g));c.x-=d.left;c.y-=d.top;return c}
function xb(a,b,c){function d(a,b,c,d,e){d=new Z(c.x+d.left,c.y+d.top,d.width,d.height);c=[0,0];b=[b.width,b.height];var f=[d.left,d.top];d=[d.width,d.height];for(var g=0;2>g;g++)if(d[g]>b[g])c[g]=e?f[g]+d[g]/2-b[g]/2:f[g];else{var h=f[g]-b[g]+d[g];0<h?c[g]=h:0>f[g]&&(c[g]=f[g])}e=new t(c[0],c[1]);a.scrollLeft+=e.x;a.scrollTop+=e.y}function e(a){var b=a.parentNode;vb&&b instanceof ShadowRoot&&(b=a.host);return b}for(var f=w(a),g=e(a),h;g&&g!=f.documentElement&&g!=f.body;)h=wb(g,a),d(g,new u(g.clientWidth,
g.clientHeight),h,b,c),g=e(g);h=ub(a);a=oa(a?new na(w(a)):p||(p=new na));d(f.body,a,h,b,c)};aa("_",function(a,b,c){c||(c=new Z(0,0,a.offsetWidth,a.offsetHeight));xb(a,c,b);a=ub(a);return new t(a.x+c.left,a.y+c.top)});; return this._.apply(null,arguments);}.apply({navigator:typeof window!=undefined?window.navigator:null,document:typeof window!=undefined?window.document:null}, arguments);}
