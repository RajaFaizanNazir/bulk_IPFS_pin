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

```sh
mkdir images
```

paste all images in the 'images' folder
 
 ```sh
 pip install -r requirements.txt
 ```
 
 ```sh
 python3 main.py
 ```
 or just run run.bat
 
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
