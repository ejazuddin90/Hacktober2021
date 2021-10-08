
        let UpperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        let LowerCase = 'abcdefghijklmnopqrstuvwxyz';
        let Numbers = '0123456789';
        let Symbols = '!@#$%^&*()';

        let genPass = document.getElementById('genPass');
        genPass.addEventListener('click', function () {
            let addLength = document.getElementById('addLength');
            // console.log(addLength.value); 
            let upperCase = document.getElementById('upperCase');
            let lowerCase = document.getElementById('lowerCase');
            let numbers = document.getElementById('numbers');
            let symbols = document.getElementById('symbols');
            let fetchData = '';
            if (upperCase.checked) {
                // console.log(1);
                fetchData += UpperCase;
            }
            if (lowerCase.checked) {
                // console.log(2);
                fetchData += LowerCase;
            }
            if (numbers.checked) {
                // console.log(3);
                fetchData += Numbers;
            }
            if (symbols.checked) {
                // console.log(4);
                fetchData += Symbols;
            }
            let addPass = '';
            for (let i = 0; i < addLength.value; i++) {
                let Password = Math.floor(Math.random() * fetchData.length);
                // console.log(Password);
                addPass += fetchData[Password];
            }
            document.getElementById('addPass').value = addPass;
        });


        function myFunction() {
            var copyText = document.getElementById("addPass");
            copyText.select();
            copyText.setSelectionRange(0, 99999);
            document.execCommand("copy");
        }