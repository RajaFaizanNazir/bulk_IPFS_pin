# bulk_IPFS_pin

### Testing on
* Ubuntu
* Windows 11
### Pre Req
* Python
* Pip (Package manager of Python)
>If python is not installed in your Windows machine, click on install_python.bat
> 
> Linux's folks already know how to install python ;p

>> Guide to run the progrma

```sh
git clone https://github.com/RajaFaizanNazir/bulk_IPFS_pin.git
```

```sh
cd bulk_IPFS_pin
```

paste all images in the 'images' and 'jsons' folder in the data folder

## File Structure
```sh
.
├── main.py
├── requirement.txt
├── constants/
│     └──── env.json
├── data/
│     ├──── images/
│     │        └───── img1.png
│     │
│     └──── jsons/
│              └───── img1.json
└── README.md
```

> If you want to give path of another parent folder, replace 'parentFolder' in env.json in constants with an absolute path

 ```sh
 pip install -r requirements.txt
 ```
 
 ```sh
 python3 main.py
 ```
 or just run run.bat
