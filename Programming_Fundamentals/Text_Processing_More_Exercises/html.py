title = input()
article_content = input()

print("<h1>")
print(f"    {title}")
print("</h1>")
print("<article>")
print(f"    {article_content}")
print("</article>")

command = input()

while not command == "end of comments":
    comment = command
    print("<div>")
    print(f"    {comment}")
    print("</div>")
    
    command = input()
