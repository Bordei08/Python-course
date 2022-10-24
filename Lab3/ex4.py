def build_xml_element(tag, s, **parameters):
    result = "<" + tag + " "
    keys = list(parameters.keys())
    i = 0
    for x in keys:
        result = result +  str(x) + "= "+ "\\\""+str(parameters[str(x)]) +"\\\""
        if i < len(keys) - 1:
            result = result + ", "
        i = i + 1    

    result = result + ">" + s + "</"+ tag + ">" 
    return result


print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))  