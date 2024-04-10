;(function(win,doc){var ccao=win["cca"];var ccaoSettings=null;win.carbonReady=win.carbonReady||[];ccao.privacy=ccao.privacy||{que:[]};var getSyncUserUrl=function(){return win._ccLauncherSettings.ingestion+"/event/record/user-sync?";};var buildEventMessage=function(nameValuePairs){var data=[];data.push(["parentId",encodeURIComponent(ccao.settings.site.parentId)]);data.push(["scriptId",encodeURIComponent(ccao.settings.site.scriptId)]);data.push(["triggerId","6832865d-3a8b-4bc0-80f8-a9b174e8afe3"]);data.push(["triggerLabel","client-event"]);data.push(["eventTarget",'']);var customAttributes=[];if(nameValuePairs){for(var i in Object.keys(nameValuePairs)){customAttributes.push([i+'='+nameValuePairs[i]]);}}
data.push(["customAttributes",customAttributes.join(";")]);return data;};function setStorage(store,key,value){if(!ccao.privacy.law||typeof ccao.privacy.law!=="string"){ccao.privacy.law="unknown";}
switch(ccao.privacy.law.toLowerCase()){case "gdpr":if(ccao.privacy.gdpr.Consent){store.setItem(key,value);}
break;case "ccpa":if(ccao.privacy.ccpa.Consent){store.setItem(key,value);}
break;case "na":store.setItem(key,value);break;case "optout":case "unknown":default:break;}}
function setLocalStorage(key,value){ccao.privacy=ccao.privacy||{};ccao.privacy.que=ccao.privacy.que||[];ccao.privacy.que.push(function(){setStorage(win.localStorage,key,value);});}
function firePixel(endpoint){if(!ccao.privacy.law||typeof ccao.privacy.law!=="string"){ccao.privacy.law="unknown";}
switch(ccao.privacy.law.toLowerCase()){case "gdpr":if(ccao.privacy.gdpr.Consent){var img=new Image(1,1);img.src=endpoint;}
break;case "ccpa":if(ccao.privacy.ccpa.Consent){var img=new Image(1,1);img.src=endpoint;}
break;case "na":var img=new Image(1,1);img.src=endpoint;break;case "optout":case "unknown":default:break;}}
function pixelSync(endpoint){return function(){ccao.privacy=ccao.privacy||{};ccao.privacy.que=ccao.privacy.que||[];ccao.privacy.que.push(function(){firePixel(endpoint);});};}
function getSyncUrlParams(partnerId,useSiteId,partnerSrc){if(partnerSrc==undefined){partnerSrc=ccaoSettings.site.parentId;if(useSiteId!==undefined&&useSiteId===true)
partnerSrc=ccaoSettings.site.id;}
return 'src='+partnerSrc+'&ccsid='+ccaoSettings.session.id+'&ccuid='+ccaoSettings.user.id+'&ccpt=-1'+'&puid='+partnerId;}
function validateMd5Hash(hash){var regex=RegExp("^[a-f0-9]{32}$","gi");return hash.match(regex);}
function validateSha256Hash(hash){var regex=RegExp("^[a-f0-9]{64}$","gi");return hash.match(regex);}
function storeMd5Hash(hash,label){if(!hash||typeof hash!=="string"){hash="";}
hash=hash.toLowerCase();if(validateMd5Hash(hash)){var storageKey="cc-"+label+"-md5";setLocalStorage(storageKey,hash);if(ccaoSettings!==null)
pixelSync(getSyncUserUrl()+getSyncUrlParams(hash,false,label+"-md5"))();}
else{console.log("String is not a valid md5 hash");}}
function storeSha256Hash(hash,label){if(!hash||typeof hash!=="string"){hash="";}
hash=hash.toLowerCase();if(validateSha256Hash(hash)){var storageKey="cc-"+label+"-sha256";setLocalStorage(storageKey,hash);if(ccaoSettings!==null)
pixelSync(getSyncUserUrl()+getSyncUrlParams(hash,false,label+"-sha256"))();}
else{console.log("String is not a valid sha256 hash");}}
function api(id){var userId=id;this.syncUserIdentity=function(clientUserId,useSiteId){if(ccaoSettings!==null&&clientUserId!==undefined)
pixelSync(getSyncUserUrl()+getSyncUrlParams(clientUserId,useSiteId))();};this.getUserId=function(){return userId;};this.recordEvent=function(eventName){if(eventName&&eventName.length>0){var data=buildEventMessage();ccao.sendMessage('custom-ce-'+eventName,data,true);}};this.refreshCarbon=function(){ccao.refreshGPTTargeting();ccao.refresh();};this.storeHashedEmail=function(algorithm,hash){if(algorithm&&hash){var label="hem";if(algorithm&&typeof algorithm==="string"&&algorithm.toLowerCase()=="md5"){storeMd5Hash(hash,label);}
else if(algorithm&&typeof algorithm==="string"&&algorithm.toLowerCase()=="sha256"){storeSha256Hash(hash,label);}
else{console.log("Algorithm not supported: "+algorithm);}}};this.storeHashedTelephone=function(algorithm,hash){if(algorithm&&hash){var label="htel";if(algorithm&&typeof algorithm==="string"&&algorithm.toLowerCase()=="md5"){storeMd5Hash(hash,label);}
else if(algorithm&&typeof algorithm==="string"&&algorithm.toLowerCase()=="sha256"){storeSha256Hash(hash,label);}
else{console.log("Algorithm not supported: "+algorithm);}}};this.ready=true;};var apiReady=function(){if(win.carbonReady!==null){var readyLen=win.carbonReady.length;for(var i=0;i<readyLen;i++){win.carbonReady[i]();}}
win.carbonReady={"push":function(pushFunc){if(typeof(pushFunc)==='function')pushFunc();}};};ccao.getSettings(function(settings){ccaoSettings=settings;var localApi=new api(settings.user.id);ccao.api=Object.assign(ccao.api,localApi);win.carbonApi=ccao.api;win.carbon=win.carbonApi;apiReady();ccao.api.dispatchEvent('apiReady');});})(window,document);