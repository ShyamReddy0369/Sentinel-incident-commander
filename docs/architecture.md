# Architecture

This document outlines the high-level architecture of the Sentinel incident commander platform.

## Overview

- Backend service exposes core API endpoints.
- Chaos engine simulates infrastructure failures and incident behavior.
- Database layer stores schema, procedures, and seed data.
- Agents provide automation and orchestration capabilities.

## Components

- Backend: Flask application entry point and service wiring.
- Chaos Engine: Simulated services, fault injection, metrics, and incidents.
- Database: Oracle-compatible schema and supporting SQL assets.
- Docs: Project guidance and implementation roadmap.
