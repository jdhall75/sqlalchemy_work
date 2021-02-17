from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, aliased, backref
from database import Base


class Container(Base):
    __tablename__ = "containers"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("containers.id"))
    data = Column(String(50), unique=True)
    children = relationship("Container")
    nodes = relationship("Node", secondary="container_nodes")


class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    containers = relationship("Container", secondary="container_nodes")


class ContainerNodeAssoc(Base):
    __tablename__ = "container_nodes"
    container_id = Column(Integer, ForeignKey("containers.id"), primary_key=True)
    node_id = Column(Integer, ForeignKey("nodes.id"), primary_key=True)
    container = relationship("Container", backref=backref("container_assoc"))
    node = relationship("Node", backref=backref("node_assoc"))
