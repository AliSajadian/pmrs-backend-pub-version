# Generated by Django 3.2.19 on 2023-07-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblwBudgetcost',
            fields=[
                ('budgetcostid', models.AutoField(db_column='BudgetCostID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('bac_r', models.BigIntegerField(blank=True, db_column='BAC_R', null=True)),
                ('bac_fc', models.BigIntegerField(blank=True, db_column='BAC_FC', null=True)),
                ('eac_r', models.BigIntegerField(blank=True, db_column='EAC_R', null=True)),
                ('eac_fc', models.BigIntegerField(blank=True, db_column='EAC_FC', null=True)),
                ('ev_r', models.BigIntegerField(blank=True, db_column='EV_R', null=True)),
                ('ev_fc', models.BigIntegerField(blank=True, db_column='EV_FC', null=True)),
                ('ac_r', models.BigIntegerField(blank=True, db_column='AC_R', null=True)),
                ('ac_fc', models.BigIntegerField(blank=True, db_column='AC_FC', null=True)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=250, null=True)),
            ],
            options={
                'db_table': 'tblw_BudgetCost',
            },
        ),
        migrations.CreateModel(
            name='TblwContractdox',
            fields=[
                ('contractdoxid', models.AutoField(db_column='ContractDoxID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('contracttitle', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ContractTitle', max_length=250)),
                ('contractor', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Contractor', max_length=250)),
                ('contractdate', models.DateField(blank=True, db_column='ContractDate', null=True)),
                ('contractno', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ContractNo', max_length=50, null=True)),
                ('riderno', models.SmallIntegerField(blank=True, db_column='RiderNo', null=True)),
                ('fileaddress', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='FileAddress', max_length=250)),
            ],
            options={
                'db_table': 'tblw_ContractDox',
            },
        ),
        migrations.CreateModel(
            name='TblwCriticalaction',
            fields=[
                ('criticalactionid', models.AutoField(db_column='CriticalActionID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('criticalaction', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CriticalAction', max_length=500)),
            ],
            options={
                'db_table': 'tblw_CriticalAction',
            },
        ),
        migrations.CreateModel(
            name='TblwDateconversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthid', models.IntegerField(db_column='MonthID')),
                ('month', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Month', max_length=50)),
            ],
            options={
                'db_table': 'tblw_DateConversion',
            },
        ),
        migrations.CreateModel(
            name='TblwFinancialinfo',
            fields=[
                ('financialinfoid', models.AutoField(db_column='FinancialInfoID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('lastclaimedinvoice_r', models.BigIntegerField(blank=True, db_column='LastClaimedInvoice_R', null=True)),
                ('lastclaimedinvoice_fc', models.BigIntegerField(blank=True, db_column='LastClaimedInvoice_FC', null=True)),
                ('lci_no', models.SmallIntegerField(blank=True, db_column='LCI_No', null=True)),
                ('lastverifiedinvoice_r', models.BigIntegerField(blank=True, db_column='LastVerifiedInvoice_R', null=True)),
                ('lastverifiedinvoice_fc', models.BigIntegerField(blank=True, db_column='LastVerifiedInvoice_FC', null=True)),
                ('lvi_no', models.SmallIntegerField(blank=True, db_column='LVI_No', null=True)),
                ('lastclaimedadjustmentinvoice_r', models.BigIntegerField(blank=True, db_column='LastClaimedAdjustmentInvoice_R', null=True)),
                ('lastclaimedadjustmentinvoice_fc', models.BigIntegerField(blank=True, db_column='LastClaimedAdjustmentInvoice_FC', null=True)),
                ('lcai_no', models.SmallIntegerField(blank=True, db_column='LCAI_No', null=True)),
                ('lastverifiedadjustmentinvoice_r', models.BigIntegerField(blank=True, db_column='LastVerifiedAdjustmentInvoice_R', null=True)),
                ('lastverifiedadjustmentinvoice_fc', models.BigIntegerField(blank=True, db_column='LastVerifiedAdjustmentInvoice_FC', null=True)),
                ('lvai_no', models.SmallIntegerField(blank=True, db_column='LVAI_No', null=True)),
                ('lastclaimedextraworkinvoice_r', models.BigIntegerField(blank=True, db_column='LastClaimedExtraWorkInvoice_R', null=True)),
                ('lastclaimedextraworkinvoice_fc', models.BigIntegerField(blank=True, db_column='LastClaimedExtraWorkInvoice_FC', null=True)),
                ('lcewi_no', models.SmallIntegerField(blank=True, db_column='LCEWI_No', null=True)),
                ('lastverifiedextraworkinvoice_r', models.BigIntegerField(blank=True, db_column='LastVerifiedExtraWorkInvoice_R', null=True)),
                ('lastverifiedextraworkinvoice_fc', models.BigIntegerField(blank=True, db_column='LastVerifiedExtraWorkInvoice_FC', null=True)),
                ('lvewi_no', models.SmallIntegerField(blank=True, db_column='LVEWI_No', null=True)),
                ('lastclaimbill_r', models.BigIntegerField(blank=True, db_column='LastClaimBill_R', null=True)),
                ('lastclaimbill_fc', models.BigIntegerField(blank=True, db_column='LastClaimBill_FC', null=True)),
                ('lcb_no', models.SmallIntegerField(blank=True, db_column='LCB_No', null=True)),
                ('lastclaimbillverified_r', models.BigIntegerField(blank=True, db_column='LastClaimBillVerified_R', null=True)),
                ('lastclaimbillverified_fc', models.BigIntegerField(blank=True, db_column='LastClaimBillVerified_FC', null=True)),
                ('lcbv_no', models.SmallIntegerField(blank=True, db_column='LCBV_No', null=True)),
                ('lastclaimbillrecievedamount_r', models.BigIntegerField(blank=True, db_column='LastClaimBillRecievedAmount_R', null=True)),
                ('lastclaimbillrecievedamount_fc', models.BigIntegerField(blank=True, db_column='LastClaimBillRecievedAmount_FC', null=True)),
                ('cumulativeclientpayment_r', models.BigIntegerField(blank=True, db_column='CumulativeClientPayment_R', null=True)),
                ('cumulativeclientpayment_fc', models.BigIntegerField(blank=True, db_column='CumulativeClientPayment_FC', null=True)),
                ('clientprepaymentdeferment_r', models.BigIntegerField(blank=True, db_column='ClientPrepaymentDeferment_R', null=True)),
                ('clientprepaymentdeferment_fc', models.BigIntegerField(blank=True, db_column='ClientPrepaymentDeferment_FC', null=True)),
                ('estcost_r', models.BigIntegerField(blank=True, db_column='EstCost_R', null=True)),
                ('estcost_fc', models.BigIntegerField(blank=True, db_column='EstCost_FC', null=True)),
                ('estclientpayment_r', models.BigIntegerField(blank=True, db_column='EstClientPayment_R', null=True)),
                ('estclientpayment_fc', models.BigIntegerField(blank=True, db_column='EstClientPayment_FC', null=True)),
                ('estdebitcredit_r', models.BigIntegerField(blank=True, db_column='EstDebitCredit_R', null=True)),
                ('estdebitcredit_fc', models.BigIntegerField(blank=True, db_column='EstDebitCredit_FC', null=True)),
            ],
            options={
                'db_table': 'tblw_FinancialInfo',
            },
        ),
        migrations.CreateModel(
            name='TblwHse',
            fields=[
                ('hseid', models.AutoField(db_column='HSEID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('totaloperationdays', models.IntegerField(blank=True, db_column='TotalOperationDays', null=True)),
                ('withouteventdays', models.IntegerField(blank=True, db_column='WithoutEventDays', null=True)),
                ('deathno', models.IntegerField(blank=True, db_column='DeathNo', null=True)),
                ('woundno', models.IntegerField(blank=True, db_column='WoundNo', null=True)),
                ('disadnantageeventno', models.IntegerField(blank=True, db_column='DisadnantageEventNo', null=True)),
            ],
            options={
                'db_table': 'tblw_HSE',
            },
        ),
        migrations.CreateModel(
            name='TblwInvoice',
            fields=[
                ('invoiceid', models.AutoField(db_column='InvoiceID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('senddate', models.DateTimeField(blank=True, db_column='SendDate', null=True)),
                ('aci_g_r', models.BigIntegerField(blank=True, db_column='ACI_G_R', null=True)),
                ('aci_g_fc', models.BigIntegerField(blank=True, db_column='ACI_G_FC', null=True)),
                ('aca_g_r', models.BigIntegerField(blank=True, db_column='ACA_G_R', null=True)),
                ('aca_g_fc', models.BigIntegerField(blank=True, db_column='ACA_G_FC', null=True)),
                ('ew_g_r', models.BigIntegerField(blank=True, db_column='EW_G_R', null=True)),
                ('ew_g_fc', models.BigIntegerField(blank=True, db_column='EW_G_FC', null=True)),
                ('icc_g_r', models.BigIntegerField(blank=True, db_column='ICC_G_R', null=True)),
                ('icc_g_fc', models.BigIntegerField(blank=True, db_column='ICC_G_FC', null=True)),
                ('acc_g_r', models.BigIntegerField(blank=True, db_column='ACC_G_R', null=True)),
                ('acc_g_fc', models.BigIntegerField(blank=True, db_column='ACC_G_FC', null=True)),
                ('ewcc_g_r', models.BigIntegerField(blank=True, db_column='EWCC_G_R', null=True)),
                ('ewcc_g_fc', models.BigIntegerField(blank=True, db_column='EWCC_G_FC', null=True)),
                ('aci_n_r', models.BigIntegerField(blank=True, db_column='ACI_N_R', null=True)),
                ('aci_n_fc', models.BigIntegerField(blank=True, db_column='ACI_N_FC', null=True)),
                ('aca_n_r', models.BigIntegerField(blank=True, db_column='ACA_N_R', null=True)),
                ('aca_n_fc', models.BigIntegerField(blank=True, db_column='ACA_N_FC', null=True)),
                ('icc_n_r', models.BigIntegerField(blank=True, db_column='ICC_N_R', null=True)),
                ('icc_n_fc', models.BigIntegerField(blank=True, db_column='ICC_N_FC', null=True)),
                ('acc_n_r', models.BigIntegerField(blank=True, db_column='ACC_N_R', null=True)),
                ('acc_n_fc', models.BigIntegerField(blank=True, db_column='ACC_N_FC', null=True)),
                ('ewcc_n_r', models.BigIntegerField(blank=True, db_column='EWCC_N_R', null=True)),
                ('ewcc_n_fc', models.BigIntegerField(blank=True, db_column='EWCC_N_FC', null=True)),
                ('ew_n_r', models.BigIntegerField(blank=True, db_column='EW_N_R', null=True)),
                ('ew_n_fc', models.BigIntegerField(blank=True, db_column='EW_N_FC', null=True)),
                ('cvat_r', models.BigIntegerField(blank=True, db_column='CVAT_R', null=True)),
                ('cvat_fc', models.BigIntegerField(blank=True, db_column='CVAT_FC', null=True)),
                ('cpi_r', models.BigIntegerField(blank=True, db_column='CPI_R', null=True)),
                ('cpi_fc', models.BigIntegerField(blank=True, db_column='CPI_FC', null=True)),
                ('ccpi_a_r', models.BigIntegerField(blank=True, db_column='CCPI_A_R', null=True)),
                ('ccpi_a_fc', models.BigIntegerField(blank=True, db_column='CCPI_A_FC', null=True)),
                ('ccpi_a_vat_r', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_R', null=True)),
                ('ccpi_a_vat_fc', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_FC', null=True)),
                ('ccpi_a_vat_ew_r', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_EW_R', null=True)),
                ('ccpi_a_vat_ew_fc', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_EW_FC', null=True)),
                ('cp_pp_r', models.BigIntegerField(blank=True, db_column='CP_PP_R', null=True)),
                ('cp_pp_fc', models.BigIntegerField(blank=True, db_column='CP_PP_FC', null=True)),
                ('pp_pp_r', models.BigIntegerField(blank=True, db_column='PP_PP_R', null=True)),
                ('pp_pp_fc', models.BigIntegerField(blank=True, db_column='PP_PP_FC', null=True)),
                ('r', models.BooleanField(blank=True, db_column='R', null=True)),
                ('m', models.BooleanField(blank=True, db_column='M', null=True)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=500, null=True)),
            ],
            options={
                'db_table': 'tblw_Invoice',
            },
        ),
        migrations.CreateModel(
            name='TblwInvoicedox',
            fields=[
                ('invoicedoxid', models.AutoField(db_column='InvoiceDoxID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('invoicekind', models.SmallIntegerField(db_column='InvoiceKind')),
                ('invoiceno', models.IntegerField(db_column='InvoiceNo')),
                ('invoicedate', models.DateField(db_column='InvoiceDate')),
                ('senddate', models.DateField(blank=True, db_column='SendDate', null=True)),
                ('confirmdate', models.DateField(blank=True, db_column='ConfirmDate', null=True)),
                ('sgp_r', models.IntegerField(blank=True, db_column='SGP_R', null=True)),
                ('sgp_fc', models.BigIntegerField(blank=True, db_column='SGP_FC', null=True)),
                ('cgp_r', models.IntegerField(blank=True, db_column='CGP_R', null=True)),
                ('cgp_fc', models.BigIntegerField(blank=True, db_column='CGP_FC', null=True)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=250, null=True)),
                ('address', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Address', max_length=250, null=True)),
                ('active', models.BooleanField(db_column='Active')),
            ],
            options={
                'db_table': 'tblw_InvoiceDox',
            },
        ),
        migrations.CreateModel(
            name='TblwInvoiceex',
            fields=[
                ('invoiceid', models.AutoField(db_column='InvoiceID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('senddate', models.DateTimeField(blank=True, db_column='SendDate', null=True)),
                ('invoicetype', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='InvoiceType', max_length=1)),
                ('alino', models.IntegerField(blank=True, db_column='ALINo', null=True)),
                ('almino', models.IntegerField(blank=True, db_column='ALMINo', null=True)),
                ('aci_g_r', models.BigIntegerField(blank=True, db_column='ACI_G_R', null=True)),
                ('aci_g_fc', models.BigIntegerField(blank=True, db_column='ACI_G_FC', null=True)),
                ('aca_g_r', models.BigIntegerField(blank=True, db_column='ACA_G_R', null=True)),
                ('aca_g_fc', models.BigIntegerField(blank=True, db_column='ACA_G_FC', null=True)),
                ('ew_g_r', models.BigIntegerField(blank=True, db_column='EW_G_R', null=True)),
                ('ew_g_fc', models.BigIntegerField(blank=True, db_column='EW_G_FC', null=True)),
                ('icc_g_r', models.BigIntegerField(blank=True, db_column='ICC_G_R', null=True)),
                ('icc_g_fc', models.BigIntegerField(blank=True, db_column='ICC_G_FC', null=True)),
                ('acc_g_r', models.BigIntegerField(blank=True, db_column='ACC_G_R', null=True)),
                ('acc_g_fc', models.BigIntegerField(blank=True, db_column='ACC_G_FC', null=True)),
                ('ewcc_g_r', models.BigIntegerField(blank=True, db_column='EWCC_G_R', null=True)),
                ('ewcc_g_fc', models.BigIntegerField(blank=True, db_column='EWCC_G_FC', null=True)),
                ('aci_n_r', models.BigIntegerField(blank=True, db_column='ACI_N_R', null=True)),
                ('aci_n_fc', models.BigIntegerField(blank=True, db_column='ACI_N_FC', null=True)),
                ('aca_n_r', models.BigIntegerField(blank=True, db_column='ACA_N_R', null=True)),
                ('aca_n_fc', models.BigIntegerField(blank=True, db_column='ACA_N_FC', null=True)),
                ('icc_n_r', models.BigIntegerField(blank=True, db_column='ICC_N_R', null=True)),
                ('icc_n_fc', models.BigIntegerField(blank=True, db_column='ICC_N_FC', null=True)),
                ('acc_n_r', models.BigIntegerField(blank=True, db_column='ACC_N_R', null=True)),
                ('acc_n_fc', models.BigIntegerField(blank=True, db_column='ACC_N_FC', null=True)),
                ('ewcc_n_r', models.BigIntegerField(blank=True, db_column='EWCC_N_R', null=True)),
                ('ewcc_n_fc', models.BigIntegerField(blank=True, db_column='EWCC_N_FC', null=True)),
                ('ew_n_r', models.BigIntegerField(blank=True, db_column='EW_N_R', null=True)),
                ('ew_n_fc', models.BigIntegerField(blank=True, db_column='EW_N_FC', null=True)),
                ('cvat_r', models.BigIntegerField(blank=True, db_column='CVAT_R', null=True)),
                ('cvat_fc', models.BigIntegerField(blank=True, db_column='CVAT_FC', null=True)),
                ('cpi_r', models.BigIntegerField(blank=True, db_column='CPI_R', null=True)),
                ('cpi_fc', models.BigIntegerField(blank=True, db_column='CPI_FC', null=True)),
                ('ccpi_a_r', models.BigIntegerField(blank=True, db_column='CCPI_A_R', null=True)),
                ('ccpi_a_fc', models.BigIntegerField(blank=True, db_column='CCPI_A_FC', null=True)),
                ('ccpi_a_vat_r', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_R', null=True)),
                ('ccpi_a_vat_fc', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_FC', null=True)),
                ('ccpi_a_vat_ew_r', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_EW_R', null=True)),
                ('ccpi_a_vat_ew_fc', models.BigIntegerField(blank=True, db_column='CCPI_A_VAT_EW_FC', null=True)),
                ('cp_pp_r', models.BigIntegerField(blank=True, db_column='CP_PP_R', null=True)),
                ('cp_pp_fc', models.BigIntegerField(blank=True, db_column='CP_PP_FC', null=True)),
                ('pp_pp_r', models.BigIntegerField(blank=True, db_column='PP_PP_R', null=True)),
                ('pp_pp_fc', models.BigIntegerField(blank=True, db_column='PP_PP_FC', null=True)),
                ('r', models.BooleanField(blank=True, db_column='R', null=True)),
                ('m', models.BooleanField(blank=True, db_column='M', null=True)),
                ('typevalue', models.SmallIntegerField(blank=True, db_column='TypeValue', null=True)),
            ],
            options={
                'db_table': 'tblw_InvoiceEx',
            },
        ),
        migrations.CreateModel(
            name='TblwMachinary',
            fields=[
                ('machinaryid', models.AutoField(db_column='MachinaryID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('machine', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Machine', max_length=50)),
                ('activeno', models.IntegerField(db_column='ActiveNo')),
                ('inactiveno', models.IntegerField(db_column='InactiveNo')),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=100, null=True)),
            ],
            options={
                'db_table': 'tblw_Machinary',
            },
        ),
        migrations.CreateModel(
            name='TblwPmsprogress',
            fields=[
                ('pmsprogressid', models.AutoField(db_column='PMSProgressID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('item', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Item', max_length=200)),
                ('lastplanprogress', models.IntegerField(blank=True, db_column='LastPlanProgress', null=True)),
                ('lastplanvirtualprogress', models.IntegerField(blank=True, db_column='LastPlanVirtualProgress', null=True)),
            ],
            options={
                'db_table': 'tblw_PMSProgress',
            },
        ),
        migrations.CreateModel(
            name='TblwProblem',
            fields=[
                ('problemid', models.AutoField(db_column='ProblemID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('problem', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Problem', max_length=500)),
            ],
            options={
                'db_table': 'tblw_Problem',
            },
        ),
        migrations.CreateModel(
            name='TblwProgressstate',
            fields=[
                ('progressstateid', models.AutoField(db_column='ProgressStateID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('plan_replan', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Plan_Replan', max_length=3)),
                ('pp_e', models.DecimalField(db_column='PP_E', decimal_places=2, max_digits=6)),
                ('ap_e', models.DecimalField(db_column='AP_E', decimal_places=2, max_digits=6)),
                ('pp_p', models.DecimalField(db_column='PP_P', decimal_places=2, max_digits=6)),
                ('ap_p', models.DecimalField(db_column='AP_P', decimal_places=2, max_digits=6)),
                ('pp_c', models.DecimalField(db_column='PP_C', decimal_places=2, max_digits=6)),
                ('ap_c', models.DecimalField(db_column='AP_C', decimal_places=2, max_digits=6)),
                ('pp_t', models.DecimalField(db_column='PP_T', decimal_places=2, max_digits=6)),
                ('ap_t', models.DecimalField(db_column='AP_T', decimal_places=2, max_digits=6)),
                ('pr_t', models.DecimalField(db_column='PR_T', decimal_places=2, max_digits=6)),
                ('pfc_t', models.DecimalField(db_column='PFC_T', decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'tblw_ProgressState',
            },
        ),
        migrations.CreateModel(
            name='TblwProjectpersonel',
            fields=[
                ('projectpersonelid', models.AutoField(db_column='ProjectPersonelID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('dpno', models.IntegerField(db_column='DPNo')),
                ('dcpno', models.IntegerField(db_column='DCPNo')),
                ('mepno', models.IntegerField(db_column='MEPNo')),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=100, null=True)),
            ],
            options={
                'db_table': 'tblw_ProjectPersonel',
            },
        ),
        migrations.CreateModel(
            name='TblwReportconfirm',
            fields=[
                ('reportconfirmid', models.AutoField(db_column='ReportConfirmID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('type', models.SmallIntegerField(blank=True, db_column='Type', null=True)),
                ('user_c', models.BooleanField(blank=True, db_column='User_C', null=True)),
                ('pm_c', models.BooleanField(blank=True, db_column='PM_C', null=True)),
                ('sa_c', models.BooleanField(blank=True, db_column='SA_C', null=True)),
                ('userconfirmdate', models.DateField(blank=True, db_column='UserConfirmDate', null=True)),
                ('pmconfirmdate', models.DateField(blank=True, db_column='PMConfirmDate', null=True)),
                ('saconfirmdate', models.DateField(blank=True, db_column='SAConfirmDate', null=True)),
            ],
            options={
                'db_table': 'tblw_ReportConfirm',
            },
        ),
        migrations.CreateModel(
            name='TblwReportdate',
            fields=[
                ('dateid', models.AutoField(db_column='DateID', primary_key=True, serialize=False)),
                ('year', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Year', max_length=10)),
                ('month', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Month', max_length=10)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
            ],
            options={
                'db_table': 'tblw_ReportDate',
            },
        ),
        migrations.CreateModel(
            name='TblwReportdox',
            fields=[
                ('reportdoxid', models.AutoField(db_column='ReportDoxID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(blank=True, db_column='DateID')),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('doctype', models.SmallIntegerField(db_column='DocType')),
                ('doctitle', models.SmallIntegerField(blank=True, db_column='DocTitle', null=True)),
                ('dockind', models.SmallIntegerField(blank=True, db_column='DocKind', null=True)),
                ('docno', models.IntegerField(blank=True, db_column='DocNo', null=True)),
                ('description', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=250)),
                ('address', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Address', max_length=250)),
                ('active', models.BooleanField(blank=True, db_column='Active', null=True)),
            ],
            options={
                'db_table': 'tblw_ReportDox',
            },
        ),
        migrations.CreateModel(
            name='TblwReportvisitdate',
            fields=[
                ('visitreportdateid', models.AutoField(db_column='VisitReportDateID', primary_key=True, serialize=False)),
                ('visitreportid', models.IntegerField(db_column='VisitReportID')),
                ('reportid', models.IntegerField(db_column='ReportID')),
                ('reportvisitdate', models.DateField(db_column='ReportVisitDate')),
            ],
            options={
                'db_table': 'tblw_ReportVisitDate',
            },
        ),
        migrations.CreateModel(
            name='TblwTimeprogressstate',
            fields=[
                ('timeprogressstateid', models.AutoField(db_column='TimeProgressStateID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('plan_replan', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Plan_Replan', max_length=3)),
                ('eep_date', models.DateField(blank=True, db_column='EEP_Date', null=True)),
                ('eee_date', models.DateField(blank=True, db_column='EEE_Date', null=True)),
                ('epp_date', models.DateField(blank=True, db_column='EPP_Date', null=True)),
                ('epe_date', models.DateField(blank=True, db_column='EPE_Date', null=True)),
                ('ecp_date', models.DateField(blank=True, db_column='ECP_Date', null=True)),
                ('ece_date', models.DateField(blank=True, db_column='ECE_Date', null=True)),
                ('epjp_date', models.DateField(blank=True, db_column='EPjP_Date', null=True)),
                ('epje_date', models.DateField(blank=True, db_column='EPjE_Date', null=True)),
            ],
            options={
                'db_table': 'tblw_TimeProgressState',
            },
        ),
        migrations.CreateModel(
            name='TblwWorkvolume',
            fields=[
                ('workvolumeid', models.AutoField(db_column='WorkVolumeID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('work', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Work', max_length=200)),
                ('planestimate', models.IntegerField(blank=True, db_column='PlanEstimate', null=True)),
                ('totalestimate', models.IntegerField(blank=True, db_column='TotalEstimate', null=True)),
                ('executedsofar', models.IntegerField(blank=True, db_column='ExecutedSoFar', null=True)),
            ],
            options={
                'db_table': 'tblw_WorkVolume',
            },
        ),
        migrations.CreateModel(
            name='TblwZone',
            fields=[
                ('zoneid', models.AutoField(db_column='ZoneID', primary_key=True, serialize=False)),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('zone', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Zone', max_length=50)),
            ],
            options={
                'db_table': 'tblw_Zone',
            },
        ),
        migrations.CreateModel(
            name='TblwZoneimage',
            fields=[
                ('zoneimageid', models.AutoField(db_column='ZoneImageID', primary_key=True, serialize=False)),
                ('zoneid', models.IntegerField(db_column='ZoneID')),
                ('dateid', models.IntegerField(blank=True, db_column='DateID')),
                ('ppp', models.DecimalField(blank=True, db_column='PPP', decimal_places=2, max_digits=6, null=True)),
                ('app', models.DecimalField(blank=True, db_column='APP', decimal_places=2, max_digits=6, null=True)),
                ('pic1', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Pic1', max_length=250, null=True)),
                ('description1', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description1', max_length=250, null=True)),
                ('pic2', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Pic2', max_length=250, null=True)),
                ('description2', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description2', max_length=250, null=True)),
                ('pic3', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Pic3', max_length=250, null=True)),
                ('description3', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description3', max_length=250, null=True)),
            ],
            options={
                'db_table': 'tblw_ZoneImage',
            },
        ),
        migrations.CreateModel(
            name='TblwReportvisit',
            fields=[
                ('reportvisitid', models.AutoField(db_column='ReportVisitID', primary_key=True, serialize=False)),
                ('userid', models.IntegerField(db_column='UserID')),
                ('contractid', models.IntegerField(db_column='ContractID')),
                ('dateid', models.IntegerField(db_column='DateID')),
                ('financialinfo', models.BooleanField(db_column='FinancialInfo')),
                ('hse', models.BooleanField(db_column='HSE')),
                ('progressstate', models.BooleanField(db_column='ProgressState')),
                ('timeprogressstate', models.BooleanField(db_column='TimeProgressState')),
                ('invoice', models.BooleanField(db_column='Invoice')),
                ('financialinvoice', models.BooleanField(db_column='FinancialInvoice')),
                ('workvolume', models.BooleanField(db_column='WorkVolume')),
                ('pmsprogress', models.BooleanField(db_column='PMSProgress')),
                ('budget', models.BooleanField(db_column='Budget')),
                ('machinary', models.BooleanField(db_column='Machinary')),
                ('personel', models.BooleanField(db_column='Personel')),
                ('problems', models.BooleanField(db_column='Problems')),
                ('criticalactions', models.BooleanField(db_column='CriticalActions')),
                ('zoneimages', models.BooleanField(db_column='ZoneImages')),
                ('projectdox', models.BooleanField(db_column='ProjectDox')),
                ('durationdox', models.BooleanField(db_column='DurationDox')),
                ('dashboard_r', models.BooleanField(db_column='Dashboard_R')),
                ('dashboard_fc', models.BooleanField(db_column='Dashboard_FC')),
                ('imagereport', models.BooleanField(db_column='ImageReport')),
            ],
            options={
                'db_table': 'tblw_ReportVisit',
                'unique_together': {('userid', 'contractid', 'dateid')},
            },
        ),
    ]