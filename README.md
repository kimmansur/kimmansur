# Kim Mansur Yano

Physical therapist and neuroscience researcher turned builder of the systems that run a municipal public-health operation in Vilhena, Rondônia (Brazil).

Executive Secretary and Director of Specialized Care at the Vilhena Municipal Health Department (SEMUS); Secretary of Health in 2022–2023. MSc in Neurological Physical Therapy (UFRN), working on EEG signal analysis and brain–computer interfaces; PhD candidate at UFRN. Founder of [Mansur Consultoria](https://mansurconsultoria.com.br).

## How I build with LLMs

I treat model output as an untrusted proposal until something outside the model confirms it.

- **Verification lives outside the model.** An automated action is closed by an external check — a re-read from the system of record, a digital-signature validation, a delivery receipt — never by the agent reporting its own success.
- **Cross-model adversarial review.** Documents with legal or financial weight are attacked by a different model family against explicit acceptance criteria. Reviewers may not cite statutes or precedent from memory; anything unverified is flagged for source check.
- **Human gates on the irreversible.** Agents work freely on internal state; signing, sending, publishing and deploying stop for explicit approval.
- **Monitors measure progress, fail loudly and expire.** Watchers track whether work advances rather than whether a process is alive, alarm on their own failure, and shut themselves down when the task ends.
- **Operational knowledge as versioned procedures.** Rules learned from real incidents live in reviewed, versioned skills that agents load on demand — not in ad-hoc prompts.

## Systems

The code is private because it handles patient and government data. Happy to walk through any of it.

| System | What it does | Link |
|---|---|---|
| **SUS billing validation** | Validates hospital and outpatient production files (AIH, BPA, APAC) against the national procedure table before submission, and prices what would be lost. | [faturamento.semusvilhena.com](https://faturamento.semusvilhena.com) |
| **Provider accountability** | Monthly accountability for contracted providers: claims reconciled against the referral system, attestation and payment trail. | [prestacao-contas.semusvilhena.com](https://prestacao-contas.semusvilhena.com) |
| **SISREG Analytics** | Waiting lists, demand mapping and cost analysis on top of Brazil's national referral and scheduling system. | [sisreg.semusvilhena.com](https://sisreg.semusvilhena.com) |
| **Oxy Tracker** | Tracks administrative processes and signatures in the municipal e-protocol system, with watchdog and proof of delivery. | [processos.semusvilhena.com](https://processos.semusvilhena.com) |
| **Operations dashboards** | Real-time monitoring panels for the health network. | [painel.semusvilhena.com](https://painel.semusvilhena.com) |
| **Residency programs portal** | Evaluation, grading and records for medical and multiprofessional residency programs. | [residencias.semusvilhena.com](https://residencias.semusvilhena.com) |
| **Events portal** | Registration and certificates for health-department events. | [eventos.semusvilhena.com](https://eventos.semusvilhena.com) |
| **Gesfarma** | Pharmaceutical supply and dispensing management (staging). | [h-gesfarma.semusvilhena.com](https://h-gesfarma.semusvilhena.com) |
| **NFS-e issuer** | Multi-tenant electronic service-invoice platform with pre-flight validation. | [nfse.mansurconsultoria.com.br](https://nfse.mansurconsultoria.com.br) |
| **SIGTAP procedure table** | Competency-versioned national procedure and pricing table used by billing and pricing engines. | internal |
| **Accreditation & procurement** | Accreditation calls, procurement and public-bidding workflows under Brazil's procurement law, from technical study to national portal publication. | internal |
| **Price database** | Market price research from public procurement records to ground cost estimates. | internal |
| **Civil-society partnerships (Law 13.019)** | Document kits and review workflow for public partnerships with nonprofits. | internal |
