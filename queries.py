from database import Session
from models import Node, Container, ContainerNodeAssoc

sess = Session()

for n in sess.query(Container).filter(Container.data == "container1").all():
    print(n.data, n.id, n.parent_id, n.children)

    for child in n.children:
        print(child.nodes)
