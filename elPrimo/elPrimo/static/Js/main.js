const iconEye = document.querySelector('.eyes');

iconEye.addEventListener('click', function(){
  const icon = this.querySelector('i');
  console.log(this.nextElementSibling);

  if (this.nextElementSibling.type === 'password'){
    this.nextElementSibling.type = 'text';
    icon.classList.remove('fa-eye-slash');
    icon.classList.add('fa-eye');
  }else{
    this.nextElementSibling.type = 'password';
    icon.classList.remove('fa-eye');
    icon.classList.add('fa-eye-slash');
  }
})

const iconEye2 = document.querySelector('.eyes-2');

iconEye2.addEventListener('click', function(){
  const icon = this.querySelector('i');
  console.log(this.nextElementSibling);

  if (this.nextElementSibling.type === 'password'){
    this.nextElementSibling.type = 'text';
    icon.classList.remove('fa-eye-slash');
    icon.classList.add('fa-eye');
  }else{
    this.nextElementSibling.type = 'password';
    icon.classList.remove('fa-eye');
    icon.classList.add('fa-eye-slash');
  }
})