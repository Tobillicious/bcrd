# Physical map class

This file states the publication-facing admissible class used by every central claim in this packet.

For the frozen `N=8`, `R2_07` setting,

```text
A_R2_07 ~= direct_sum_{a=0}^6 M_{d_a}
d = (64,64,32,64,32,64,32)
m = (1,1,1,1,1,2,2)
physical trace tau(x) = sum_a m_a Tr(x_a)
```

The admissible class `C` consists of **one** map

```text
Phi : A_R2_07 -> A_R2_07
```

that is:

- completely positive;
- preserving the physical weighted trace `tau`;
- source-independent;
- time-independent;
- common to every transition in the fitted dataset;
- defined on the whole record algebra;
- allowed to use all 49 central transfers.

No dictionary, low-rank ansatz, fixed Kraus template, optimizer basin, transition-labelled map family, map-class augmentation, or hidden-state augmentation is part of `C`.

For transition `j`,

```text
e_j(Phi) = (1/2) || Lambda_j^next - Phi o Lambda_j^cur ||_diamond.
```

The factor `1/2` is load-bearing. The source channel is complete on `E00,E01,E10,E11`.

Computational P/Q support reductions in the frozen development chain are used only where hostile review established **minimax equivalence through CPTP extension/retraction**. Reduced and global map sets are not asserted to be literally equal. The constructive witnesses packaged here are whole-algebra physical CPTP maps.

Authority: PR #223 terminal `0a598dceefff780ccb1e1a25caceda4d30643997`, with the underlying map-class lineage recorded in `../AUTHORITIES.md` and `authority-manifest.md`.
