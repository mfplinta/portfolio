---
title: Cloud setup
---
## Part 1. Instance creation

Create a free account in the Oracle Cloud website. A credit card may be needed for identity verification purposes.

![[1.png]]

Even though a credit card number is required, following this tutorial correctly **should not** incur you any charges. The Always-Free instances at Oracle are free for our usage purposes up to an indefinite amount of time, in contrast to AWS’s free service for a single year.

This will allow us to spin up an ARM (aarch64) instance with 24 GBs of RAM, 4 OCPUs, and 200 GBs of disk storage, which is nothing to scuff at and can serve us way beyond our intended purpose on this guide.

![[2.png]]

Create a VM instance with the configuration:

- OCPU: 4
- Memory: 24 GB
- Storage: 200 GB

Click on change image and select:

- Canonical Ubuntu 24.04

Click on change shape, and ensure **VM.Standard.A1.Flex** is selected. Click on the small arrow to change the configuration as below:

![[3.png]]

Finally, click on “Select shape.”