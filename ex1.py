def longest_substring(str1, str2, str3):
    longest = ""
    
    for start in range(len(str1)):
        for end in range(start + 1, len(str1) + 1):
            substr = str1[start:end] 

            if substring(substr, str2) and substring(substr, str3):
                if len(substr) > len(longest):
                    longest = substr
    return longest


def substring(sub, full):
    sub_index = 0
    full_index = 0

    while sub_index < len(sub) and full_index < len(full):
        if sub[sub_index] == full[full_index]:
            sub_index += 1  
        full_index += 1  

    return sub_index == len(sub)



print(longest_substring("ADDZ", "CDDY", "UDDF")) 
print(longest_substring("UIBAZDBSIAHFB", "PQACIZDBIBDLAG", "QIDBCZDBKSHDVF")) 
print(longest_substring("UIBAZDBSIAHB", "PQACIZDBSBDLG", "QIDBCZDBSLHDVF")) 
