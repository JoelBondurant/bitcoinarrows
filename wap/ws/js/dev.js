/*
dev wip
*/

var dev = (function () {

return  {
proofOfWork: async function (x, difficulty=2) {
	nonce = 0n;
	match = "0".repeat(difficulty);
	while (true) {
		nonceStr = nonce.toString();
		hsh = await sha256(x + nonceStr);
		hsh = bytesToHex(hsh);
		if (hsh.slice(0, difficulty) == match) {
			return [hsh, nonceStr];
		}
		nonce++;
	}
}
}

})();
