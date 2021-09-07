//Async Await可以使异步执行代码逻辑更清晰。
function send() {
    return new Promise(function(resolve, reject){
        setTimeout(function() {
            resolve("Dane");
        }, 2000);
    });
};
let pms = send();

//Async Await代码部分
async function getUserN() {
    let usern = await send();
    console.log(usern);
};

getUserN();

//

function find() {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            reject("No message error")
        }, timeout);
    });
};

async function getMessage() {
    try {
        let usern = await send();
    console.log(usern);
    } catch (errorm) {
        console.log(`Error - ${errorm}`)
    };
};