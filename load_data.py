from database import Base, engine, Session
from models import Node, Container, ContainerNodeAssoc

Base.metadata.create_all(engine)

session = Session()


n1 = Container(parent_id=None, data="container1")
n2 = Container(parent_id=None, data="container2")

c1 = Container(data="child1")
c2 = Container(data="child2")
c3 = Container(data="child3")
c4 = Container(data="child4")
c5 = Container(data="child5")
c6 = Container(data="child6")

node1 = Node(name="node1")
node2 = Node(name="node2")
node3 = Node(name="node3")
node4 = Node(name="node4")
node5 = Node(name="node5")
node6 = Node(name="node6")

# populate the assoc table
# node1 in container1
node1_container1 = ContainerNodeAssoc(container=c1, node=node1)
node2_container2 = ContainerNodeAssoc(container=c2, node=node2)
node3_container3 = ContainerNodeAssoc(container=c3, node=node3)
node4_container4 = ContainerNodeAssoc(container=c4, node=node4)
node5_container5 = ContainerNodeAssoc(container=c5, node=node5)
node6_container6 = ContainerNodeAssoc(container=c6, node=node6)

session.add(node1_container1)
session.add(node2_container2)
session.add(node3_container3)
session.add(node4_container4)
session.add(node5_container5)
session.add(node6_container6)

n1.children.append(c1)
n1.children.append(c2)
n1.children.append(c3)
n2.children.append(c4)
n2.children.append(c5)
n2.children.append(c6)

session.add(c1)
session.add(c2)
session.add(c3)
session.add(c4)
session.add(c5)
session.add(c6)
session.add(n1)
session.add(n2)
session.commit()