"""A small CRUD application built around SOLID boundaries.

Layers (dependencies point inward only):

    cli  ->  services  ->  ports  <-  adapters
                  \\         |
                   ->  domain

- ``domain``   holds entities, validation, and errors. Depends on nothing.
- ``ports``    holds the abstract repository contract.
- ``adapters`` holds concrete storage implementations of the port.
- ``services`` holds the use cases, coded against the port only.
- ``cli``      is the composition root that wires everything together.
"""
