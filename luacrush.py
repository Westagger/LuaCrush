import re

def compress_lua(filename):
    with open(filename, 'r') as file:
        lua_script = file.read()
    lua_script = re.sub(r'--.*', '', lua_script)
    lua_script = re.sub(r'--\[\[(.*?)\]\]', '', lua_script, flags=re.DOTALL)
    lua_script = re.sub(r'\s+', ' ', lua_script)
    
    with open(filename, 'w') as file:
        file.write(lua_script)
