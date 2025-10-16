# 🧠 Data Engineering Portfolio

This repository showcases a **real-world Data Engineering project** developed collaboratively within a **12-member cross-functional team** as part of a business-oriented data integration initiative.

---

## 🚀 Project Overview

The project implements a **modern data ingestion and transformation pipeline** using **Azure Data Factory (ADF)** and **Databricks**, integrated with **Azure Data Lake Storage (ADLS)** for scalable and cost-efficient data management.

![ADF+Databricks ETL Pipeline](https://github.com/Kavoondev/Data-Engineering-Portfolio/blob/main/assets/etl_arch.jpg)

It automates the full **ETL/ELT lifecycle** — from metadata-driven ingestion to Delta Lake–based curation — ensuring consistency, flexibility, and observability across all data entities.

---

## 🧩 Architecture Highlights

- **Azure Data Factory (ADF):**
  - Orchestrates metadata-driven pipelines with dynamic activity creation.
  - Integrates Databricks notebooks for transformation, validation, and DDL automation.
  - Sends status notifications (Success/Failed) to Microsoft Teams via webhook.

- **Azure Databricks:**
  - Executes parameterized ETL notebooks for each entity.
  - Performs schema validation, CDC (Change Data Capture), and Delta Merge.
  - Maintains external Delta tables on ADLS (metadata-only persistence).

- **Azure Data Lake Storage (ADLS):**
  - Multi-layer architecture: *Raw → Bronze → Silver*.
  - Each layer is versioned, validated, and optimized for incremental processing.

---

## 🌟 Unique Features

1. **Metadata-driven automation** — all ingestion logic (source, target, columns, filters) is dynamically loaded from a metadata file, allowing rapid onboarding of new entities **without code changes**.  
2. **Unified DDL execution framework** — dynamically runs DDL notebooks that auto-create external Delta tables, reporting structured JSON results back to ADF.

---

## 👥 Team & Scope

- **Total Integration Team:** 5 engineers (including me) responsible for designing and implementing the **data ingestion and transformation pipelines**.  
- This repository presents my individual contribution — the **Integration component** of the overall platform.

---

## ⚙️ Tech Stack

| Area | Technologies |
|------|---------------|
| Orchestration | Azure Data Factory |
| Transformation | Azure Databricks (PySpark, Delta Lake) |
| Storage | Azure Data Lake Storage Gen2 |
| Automation | Metadata-driven JSON configuration |
| Notification | Microsoft Teams Webhook |
| Governance | Control tables, audit logs, DDL validation |

---

## 📈 Key Outcomes

- Reduced manual configuration effort by **80%** through metadata-driven pipeline logic.  
- Ensured **idempotent and incremental data ingestion** with automatic schema validation.  
- Achieved **high observability** via structured pipeline logging and notification system.

---

## 📂 Structure

/integration/
├── adf_pipeline_templates/
├── notebooks/
│ ├── etl/
│ ├── ddl/
│ └── shared_utils/
├── metadata/
│ └── entities_config.json
└── docs/
└── pipeline_design.md

---

## 🧭 Future Enhancements

- Add **automated data quality tests** using Great Expectations.  
- Extend **streaming ingestion** with Structured Streaming (Databricks).  
- Implement **CI/CD** for ADF + Databricks deployment (YAML pipelines).

---

*Created as part of a real-world enterprise integration project to demonstrate scalable, metadata-driven data engineering on Azure.*