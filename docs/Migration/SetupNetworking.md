## Setup Networking on AWS

1. Go to [AWS Console](https://console.aws.amazon.com/console/home?region=us-east-1#)
2. Type `VPC` on the textbox and click the VPC menu
    ![](../../images/Migration/SetupNetworking/2.png)
3. Click `Your VPCs` at the left side of the menu
    ![](../../images/Migration/SetupNetworking/3.png)
4. Click `Create VPC`
    ![](../../images/Migration/SetupNetworking/4.png)
5. Fill the Name Tag as `DatabaseVPC`
6. Fill the IPv4 CIDR block as `10.0.0.0/16`
7. Click `Create VPC` button
    ![](../../images/Migration/SetupNetworking/7.png)
8. On the left menu, click `Subnets`
    ![](../../images/Migration/SetupNetworking/8.png)
9. Click `Create Subnet`
    ![](../../images/Migration/SetupNetworking/9.png)
10. Fill the Name Tag as `Public1`
11. Choose the previous VPC that has been created (`DatabaseVPC`)
12. Choose Availability Zone as `us-east-1a`
13. Fill 1Pv4 CIDR block as `10.0.0.0/24`
    ![](../../images/Migration/SetupNetworking/13.png)
14. Click `Create`
15. Click `Close`
16. Click `Create Subnet`
17. Fill the Name Tag as `Public2`
18. Choose the previous VPC that has been created (`DatabaseVPC`)
19. Choose Availability Zone as `us-east-1b`
20. Fill 1Pv4 CIDR block as `10.0.1.0/24`
    ![](../../images/Migration/SetupNetworking/20.png)
21. Click `Create`
22. Click `Close`
23. Click `Internet Gateways` at the left menu
    ![](../../images/Migration/SetupNetworking/23.png)
24. Click `Create internet gateway`
    ![](../../images/Migration/SetupNetworking/24.png)
25. Fill the Name tag `DatabaseVPCIGW`
26. Click `Create internet gateway`
27. Click `Internet Gateways` at the left menu
28. Check the checkbox of your internet gatway you have created
29. Click `Actions` and click `Attach to VPC`
    ![](../../images/Migration/SetupNetworking/29.png)
30. Choose the VPC you have previously made (`DatabaseVPC`)
31. Click `Attach internet gateway`
32. Click `Your VPCs` at the left menu
33. Check the checkbox of your VPC you have created
34. Click `Actions` and click `Edit DNS hostnames`
    ![](../../images/Migration/SetupNetworking/34.png)
35. Check DNS hostnames to `Enable`
36. Click `Save Changes`
37. Click `Route Tables` on the left menu
    ![](../../images/Migration/SetupNetworking/37.png)
38. Choose the Route Table that contains your VPC (`DatabaseVPC`)
    ![](../../images/Migration/SetupNetworking/38.png)
39. In menu below, click `Routes` and click `Edit routes`
    ![](../../images/Migration/SetupNetworking/39.png)
40. Click `Add route`
41. Fill the destination of `0.0.0.0/0`
42. on Target, choose `Internet Gateway`
43. Pick your Internet Gateway (`DatabaseVPCIGW`)
    ![](../../images/Migration/SetupNetworking/43.png)
44. Click `Save routes`
45. Click `Close`

[BACK TO WORKSHOP GUIDE](../../README.md)