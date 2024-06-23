




******

Bravo!  You have received a Medical Diploma from   
the Orbital Convergence University International Air and Water Embassy of the Tangerine Planet.  

You are now officially certified to include this module in your practice.

******


# movies_ogv

---

## description   
Make sure you use this inside a Docker container.    
It runs deletions.

---		
		
## obtain & build
```
pip install movies_ogv
```


## fernet tar
This produces a key: fernet.key.JSON   
Then produces encrypt: constant.tar.fernet   
Then produces decrypt: constant.decrypted   

These procedures search for: fernet.key.JSON
```
movies_ogv fernet_1_tar produce_key
movies_ogv fernet_1_tar encrypt --dir "constant"
movies_ogv fernet_1_tar decrypt --file "constant.tar.fernet"
```




   