# Usage

```
usage: file.py [-h] --path PATH -rt {replace, remove_start, remove_end, remove_from_to, uppercase, lowercase, set_name}
               --params PARAMS

options:
  -h, --help            show this help message and exit
  --path PATH           path to your file
  -rt, --rename-type {replace, remove_start, remove_end, remove_from_to, uppercase, lowercase, set_name}
                        choose rename type
  --params PARAMS       parameters for chosen rename type
```

# Examples
### Replace
`file.py --path="path/to/directory" --rename-type="replace" --params="old:new"`
<br>
Replace a part of the name with something else. (params takes in {old string}:{new string})

### Remove from start
`file.py --path="path/to/directory" --rename-type="remove_start" --params="3"`
<br>
Remove n chars from the start of the name. (params takes in {n chars to remove})

### Remove from end
`file.py --path="path/to/directory" --rename-type="remove_end" --params="3"`
<br>
Remove n chars from the end of the name. (params takes in {n chars to remove})

### Remove from - to
`file.py --path="path/to/directory" --rename-type="remove_from_to" --params="2:4"`
<br>
Remove chars from index1 to index2 (params takes in {index1}:{index2})

### Uppercase
`file.py --path="path/to/directory" --rename-type="uppercase" --params=""`
<br>
Set all letters to uppercase (params doesn't require anything)

### Lowercase
`file.py --path="path/to/directory" --rename-type="lowercase" --params=""`
<br>
Set all letters to lowercase (params doesn't require anything)

### Set name
`file.py --path="path/to/directory" --rename-type="set_name" --params="name:-"`
<br>
Set the name to the given name with duplicates being separated by the given separator (params takes in {name}:{separator})
