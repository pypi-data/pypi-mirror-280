from lifeomic_logging import scoped_logger
from typing import Any

from ruamel.yaml import YAML
from ingestion.nextgen.util.process_cnv import process_cnv
from ingestion.nextgen.util.process_manifest import process_manifest
from ingestion.nextgen.util.process_structural import process_structural
from ingestion.nextgen.util.process_vcf import process_vcf


def process(
    account_id: str,
    project_id: str,
    vendor_files: dict,
    local_output_dir: str,
    source_file_id: str,
    case_id: str,
    ingestion_id: str,
    phc_output_dir: str = ".lifeomic/nextgen",
) -> dict[str, Any]:
    log_context = {
        "accountId": account_id,
        "projectId": project_id,
        "archiveFileId": source_file_id,
        "caseId": case_id,
        "ingestion_id": ingestion_id,
    }
    with scoped_logger(__name__, log_context) as log:
        cnv_path_name = process_cnv(
            xml_in_file=vendor_files["xmlFile"],
            cnv_in_file=vendor_files["somaticCnvTxtFile"],
            root_path=local_output_dir,
            prefix=case_id,
            log=log,
        )
        structural_path_name = process_structural(
            xml_in_file=vendor_files["xmlFile"],
            sv_in_file=vendor_files["somaticSvVcfFile"],
            root_path=local_output_dir,
            prefix=case_id,
            log=log,
        )
        manifest = process_manifest(
            xml_in_file=vendor_files["xmlFile"],
            source_file_id=source_file_id,
            prefix=case_id,
            include_copy_number=bool(cnv_path_name),
            include_structural=bool(structural_path_name),
            log=log,
        )
        somatic_vcf_meta_data = process_vcf(
            vcf_in_file=vendor_files["somaticVcfFile"],
            root_path=local_output_dir,
            case_id=case_id,
            sequence_type="somatic",
            xml_in_file=vendor_files["xmlFile"],
            log=log,
        )
        germline_vcf_meta_data = process_vcf(
            vcf_in_file=vendor_files["germlineVcfFile"],
            root_path=local_output_dir,
            case_id=case_id,
            sequence_type="germline",
            xml_in_file=vendor_files["xmlFile"],
            log=log,
        )

    manifest_path_name = f"{local_output_dir}/{case_id}.ga4gh.genomics.yml"
    log.info(f"Saving file to {manifest_path_name}")
    with open(manifest_path_name, "w") as file:
        yaml = YAML()
        yaml.dump(manifest, file)

    # Hard-code genome reference for nextgen
    genome_reference = "GRCh38"

    nextgen_metadata = {
        "manifest_path_name": manifest_path_name,
        "cnv_path_name": cnv_path_name,
        "cnv_genome_reference": genome_reference,
        "somatic_vcf_meta_data": somatic_vcf_meta_data,
        "somatic_genome_reference": genome_reference,
        "germline_vcf_meta_data": germline_vcf_meta_data,
        "germline_genome_reference": genome_reference,
    }
    if structural_path_name:
        nextgen_metadata["structural_path_name"] = structural_path_name
        nextgen_metadata["structural_genome_reference"] = genome_reference

    return nextgen_metadata
