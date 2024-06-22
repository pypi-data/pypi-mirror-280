provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}


resource "google_compute_global_forwarding_rule" "default" {
  name                  = "${var.resource_name}-forwarding-rule"
  target                = google_compute_target_https_proxy.default.id
  port_range            = "443"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL_MANAGED"
}

resource "google_compute_target_https_proxy" "default" {
  name             = "${var.resource_name}-https-proxy"
  url_map          = google_compute_url_map.default.id
  ssl_certificates = [google_compute_managed_ssl_certificate.default.id]
}

resource "google_compute_managed_ssl_certificate" "default" {
  name = "${var.resource_name}-ssl-certificate"
  managed {
    domains = [var.domain]
  }
}

resource "google_compute_url_map" "default" {
  name = var.resource_name

  default_service = google_compute_backend_service.default.self_link
}

resource "google_compute_backend_service" "default" {
  name                  = "${var.resource_name}-backend-service"
  protocol              = "HTTPS"
  load_balancing_scheme = "EXTERNAL_MANAGED"

  backend {
    group = google_compute_region_network_endpoint_group.cloud_run_neg.self_link
  }

}

resource "google_compute_region_network_endpoint_group" "cloud_run_neg" {
  name                  = "${var.cloud_run_service}-serverless-neg"
  network_endpoint_type = "SERVERLESS"
  region                = var.region == null ? var.gcp_region : var.region
  cloud_run {
    service = var.cloud_run_service
  }
}

resource "google_storage_bucket_object" "connection_info" {
  bucket = var.artifact_bucket
  name   = "resources/${var.resource_name}.yaml"
  content = yamlencode({
    ip_address         = google_compute_global_forwarding_rule.default.ip_address
    ssl_certificate_id = google_compute_managed_ssl_certificate.default.id
  })
}


# TODO: point this at the right thing
output "gcp_id" {
  value = google_compute_url_map.default.id
}
