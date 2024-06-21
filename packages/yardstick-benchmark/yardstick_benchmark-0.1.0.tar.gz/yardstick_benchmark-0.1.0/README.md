
# Pamuk Gaming Benchmark

Pamuk is a benchmark for online games. You can check out the performance results in the results folder, or run in yourself

## Research

Pamuk is the successor of Yardstick. Together, these tools have been used in the following scientific publications:

- Pamuk
- Meterstick
- Yardstick

## TODO

- [x] Wait for server to be ready
- [x] Make sure RCON can connect to PaperMC

## Code Documentation

### An Example To Get Started

```python
import yardstick as ys
from ys import provisioning
from ys import monitoring
from ys.games.minecraft import server, workloads

prov = provisioning.Das()
monitor = monitoring.Prometheus()
mc = server.Vanilla()
workload = workloads.TeleportRandom()

nodes = prov.reserve(5)
monitor.deploy(nodes)
mc.deploy(nodes[0])
workload.deploy(nodes[1:])

mc.wait_for_ready()
workload.start()

workload.cleanup()
mc.cleanup()
monitor.cleanup()

prov.release(nodes)
```

### Providers

Nodes are provisioned through *providers* such as the DAS5/6.
They implement the following interface:

```python
class Provider:
    def provision(nodes=0) -> Reservation
    def release(r: Reservation) -> None
```

```python
class Run:
    def assign_roles(nodes, roles) -> None
```

### Experiment

```python
class Experiment:
    def setup(nodes) -> None
    def teardown(nodes) -> None
```

### Games

Pamuk benchmarks the performance of *games*.
How each game is implemented in Pamuk depends on the game in question,
but Pamuk offers helper classes for *Runnables* such as servers and clients, which are common concepts in multiplayer games.

#### Runnable

```python
class Runnable:
    def before(nodes) -> None
    def before_each(nodes) -> None
    def start(nodes) -> None
    def stop(nodes) -> None
    def after_each(nodes) -> None
    def after(nodes) -> None
```

### Workload