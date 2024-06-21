# Conduit Forge

  This project is destinated to offer a flexible structure to model piping systems in Python. This library uses classes
  to represent some common piping components, such as: Pipes, joints, elbows, connectors and etc.

## Scope/Limitations of the Project

This library is limited to model the piping systems under the conditions bellow:

    * Non-compressible flow;
    * Single phase flow;
    * Single Chemical Species;
    * Isotermic flow;
    * Adiabatic flow;

# Documentation

## Main Classes and Piping systems Objects

### Port Class

This class, is the responsible for storing the size, shape and position of the extremities of some piping component.
In the example of the inlet Port of a Pipe:

    import conduitforge as cf

    pipe_1 = cf.Pipe(internal_diam = 3, length = 12)

    print(f'\n{type(pipe.component_input_port[0]) = }')
    print(f'\n{pipe_1.component_input_port[0].geometry = }') #
    print(f'\n{pipe_1.component_input_port[0].characteristic_length = }')

    >>>type(pipe_1.component_input_port[0]) = <class__Port__>
    >>>pipe_1.component_input_port[0].geometry = 'cilyndrical
    >>>pipe_1.component_input_port[0].characteristic_length = 3

### Component Class

This class is where all the basic propperties (and behaviour) of all the components of a piping/pumping system are declared.
It isn't meant to be used directly by the user, for it was created to increase modularity and further maintenance of the code.

* Pipe: A child-class of Component, represents a cilyndrical Pipe.
* Duct: A child-class of Pipe, used for square or rectangular ducts.
* Custom_Connector: A child-class of Component, allows the user to create Custom connectors.

### Current Class

This class stores the hidraulic and thermodynamic properties of some stream of fluid, such as mass flow, chemical composition,
pressure, temperature, density viscosity and etc.

### Mosaic Class

This class maintains a list of joints made between currents, components and other objects.
