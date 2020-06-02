<! Entity='SCE'  time='2016/10/20_16:06:26' !>
<PSDSCEFPOINTCUR>
@  Dev Type NameI BaseI Loca NameJ BaseJ Par Iinter Ishort Sshort Im1 Id1 Im2 Id2 Im0 Id0 Ima Ida Imb Idb Imc Idc 
// 故障元件类型 计算类型 故障I侧名称 故障I侧电压 故障点位置 故障J侧名称 故障J侧电压 故障支路回路号 遮断电流有名值 短路电流有名值 短路容量有名值 正序短路电流 正序短路电流相角 负序短路电流 负序短路电流相角 零序短路电流 零序短路电流相角 A相短路电流 A相短路电流相角 B相短路电流 B相短路电流相角 C相短路电流 C相短路电流相角 
</PSDSCEFPOINTCUR>
<PSDSCEFPOINTRX>
@  Dev Type NameI BaseI Loca NameJ BaseJ Par R1N R1U X1N X1U R2N R2U X2N X2U R0N R0U X0N X0U 
// 故障元件类型 计算类型 故障I侧名称 故障I侧电压 故障点位置 故障J侧名称 故障J侧电压 故障支路回路号 正序电阻有名值 正序电阻标幺值 正序电抗有名值 正序电抗标幺值 负序电阻有名值 负序电阻标幺值 负序电抗有名值 负序电抗标幺值 零序电阻有名值 零序电阻标幺值 零序电抗有名值 零序电抗标幺值 
</PSDSCEFPOINTRX>
<PSDSCEBUSVOL>
@  Name Base Type Devf NameIf BaseIf Locaf NameJf BaseJf Parf Vm1N Vm1U Vd1 Vm2N Vm2U Vd2 Vm0N Vm0U Vd0 VmaN VmaU Vda VmbN VmbU Vdb VmcN VmcU Vdc 
// 节点名称 节点电压 计算类型 故障元件类型 故障I侧名称 故障I侧电压 故障点位置 故障J侧名称 故障J侧电压 故障支路回路号 正序电压有名值 正序电压标幺值 正序电压相角 负序电压有名值 负序电压标幺值 负序电压相角 零序电压有名值 零序电压标幺值 零序电压相角 A相电压有名值 A相电压标幺值 A相电压相角 B相电压有名值 B相电压标幺值 B相电压相角 C相电压有名值 C相电压标幺值 C相电压相角 
</PSDSCEBUSVOL>
<PSDSCEBUSCUR>
@  Name Base Type Devf NameIf BaseIf Locaf NameJf BaseJf Parf Im1 Id1 Im2 Id2 Im0 Id0 Ima Ida Imb Idb Imc Idc 
// 节点名称 节点电压 计算类型 故障元件类型 故障I侧名称 故障I侧电压 故障点位置 故障J侧名称 故障J侧电压 故障支路回路号 正序注入电流 正序注入电流相角 负序注入电流 负序注入电流相角 零序注入电流 零序注入电流相角 A相注入电流 A相注入电流相角 B相注入电流 B相注入电流相角 C相注入电流 C相注入电流相角 
</PSDSCEBUSCUR>
<PSDSCEBRANCHCUR>
@  Branch NameI BaseI Type NameJ BaseJ Par Devf NameIf BaseIf Locaf NameJf BaseJf Parf Im1 Id1 Im2 Id2 Im0 Id0 Ima Ida Imb Idb Imc Idc 
// 支路类型 I侧节点名称 I侧节点电压 计算类型 J侧节点名称 J侧节点电压 支路回路号 故障元件类型 故障I侧名称 故障I侧电压 故障点位置 故障J侧名称 故障J侧电压 故障支路回路号 正序电流 正序电流相角 负序电流 负序电流相角 零序电流 零序电流相角 A相电流 A相电流相角 B相电流 B相电流相角 C相电流 C相电流相角 
</PSDSCEBRANCHCUR>
<PSDSCEBRANCHDSF>
@  Branch NameI BaseI Type NameJ BaseJ Par Devf NameIf BaseIf Locaf NameJf BaseJf Parf Ishor Dshort Fdis Ioff Doff 
// 支路类型 I侧节点名称 I侧节点电压 计算类型 J侧节点名称 J侧节点电压 支路回路号 故障元件类型 故障I侧名称 故障I侧电压 故障点位置 故障J侧名称 故障J侧电压 故障支路回路号 短路时支路电流 短路时支路电流相角 支路电流分布系数 支路断开时短路电流 支路断开时短路电流相角 
</PSDSCEBRANCHDSF>
<PSDSCEEQUBUS>
@  Name Base Type G1N G1U B1N B1U G2N G2U B2N B2U G0N G0U B0N B0U Im Id 
// 等值节点名称 等值节点电压 计算类型 正序电导有名值 正序电导标幺值 正序电钠有名值 正序电钠标幺值 负序电导有名值 负序电导标幺值 负序电钠有名值 负序电钠标幺值 零序电导有名值 零序电导标幺值 零序电钠有名值 零序电钠标幺值 注入电流 注入电流相角 
#  '母线1   ' 230 12 0.00252358 1.33497 -0.0183688 -9.71709 0.00252358 1.33497 -0.0183688 -9.71709 1.11318e-005 0.00588874 0.000316506 0.167431 2.46211 -82.1774 
#  '母线2   ' 230 12 0.00251517 1.33053 -0.0118184 -6.25195 0.00251517 1.33053 -0.0118184 -6.25195 -5.98594e-006 -0.00316656 0.000269602 0.142619 1.60452 -77.9857 
#  '母线3   ' 230 12 0.00134449 0.711236 -0.0103995 -5.50134 0.00134449 0.711236 -0.0103995 -5.50134 -2.90206e-006 -0.00153519 0.000290664 0.153761 1.39245 -82.6334 
</PSDSCEEQUBUS>
<PSDSCEEQUBRANCH>
@  NameI BaseI Type NameJ BaseJ R1N R1U X1N X1U R2N R2U X2N X2U R0N R0U X0N X0U 
// I侧节点名称 I侧节点电压 计算类型 J侧节点名称 J侧节点电压 正序电阻有名值 正序电阻标幺值 正序电抗有名值 正序电抗标幺值 负序电阻有名值 负序电阻标幺值 负序电抗有名值 负序电抗标幺值 零序电阻有名值 零序电阻标幺值 零序电抗有名值 零序电抗标幺值 
#  '母线1   ' 230 12 '母线2   ' 230 14.2497 0.026937 135.68 0.256485 14.2497 0.026937 135.68 0.256485 150.618 0.284723 354.461 0.670058 
#  '母线1   ' 230 12 '母线3   ' 230 23.0794 0.0436284 143.037 0.270391 23.0794 0.0436284 143.037 0.270391 188.863 0.35702 352.984 0.667266 
#  '母线2   ' 230 12 '母线3   ' 230 7.24198 0.0136899 93.3039 0.176378 7.24198 0.0136899 93.3039 0.176378 80.6515 0.15246 269.536 0.509519 
</PSDSCEEQUBRANCH>
<PSDSCEZMATRIX>
@  NameI BaseI NameJ BaseJ Rij Xij
// I侧节点名称 I侧节点电压 J侧节点名称 J侧节点电压 互(自)电阻 互(自)电抗
</PSDSCEZMATRIX>
<PSDSCEBASICINFO>
@  CalTime PrgVsn ReturnCode 
// 当前时间 程序版本号 程序返回值 
#  1476950786 2.3.0 0
</PSDSCEBASICINFO>
<PSDSCEERRORINFO>
@  Type KeyType NameI VoltI NameJ VoltJ Par Info 
// 错误类型 出错元件类型 I侧节点名称 I侧节点电压 J侧节点名称 J侧节点电压 回路号 错误信息 
</PSDSCEERRORINFO>
