import { useMemo } from 'react';
import { PageHeader } from '../components/PageHeader';
import { usePhaseData } from '../hooks/usePhaseData';
import { useRevenuePlan } from '../hooks/useRevenuePlan';
import { journeyMessagingExamples } from '../data/journeyMessaging';
import { translationGuardrailStack } from '../data/translationGuardrails';
import type { RevenueBundle } from '../types/revenue';
import { useArticlesStore } from '../store';

const Home = () => {
  const { articles, featuredCategory, setFeaturedCategory } = useArticlesStore();
  const { progress, readiness, status: readinessStatus, source: readinessSource } = usePhaseData();
  const { plan: revenuePlan, status: revenueStatus, source: revenueSource } = useRevenuePlan();

  const featuredArticles = useMemo(
    () => articles.filter((article) => article.category === featuredCategory),
    [articles, featuredCategory],
  );

  const categories = useMemo(() => Array.from(new Set(articles.map((a) => a.category))), [articles]);
  const readinessLoaded = readinessStatus !== 'loading' && readiness;
  const revenueLoaded = revenueStatus !== 'loading' && revenuePlan;
  const bundleLookup = useMemo(() => {
    const entries: Record<string, RevenueBundle> = {};
    revenuePlan.bundles.forEach((bundle) => {
      entries[bundle.bundle_id] = bundle;
    });
    return entries;
  }, [revenuePlan]);

  return (
    <section>
      <PageHeader
        title="Curate tomorrow's headlines"
        subtitle="Prototype the NewsKoo experience with curated story stacks, transparency logs, and category cadences."
        actions={
          <div>
            <button type="button">Book a Demo</button>
            <button type="button" style={{ background: 'transparent', color: '#fcd34d', border: '1px solid #fcd34d' }}>
              Explore Docs
            </button>
          </div>
        }
      />

      <div className="panel">
        <h2>Featured focus</h2>
        <p>Spotlight a category to see which cards already include Phase 003~007 guardrails.</p>
        <div className="pill-group">
          {categories.map((category) => (
            <button
              key={category}
              type="button"
              onClick={() => setFeaturedCategory(category)}
              className={`pill ${category === featuredCategory ? 'active' : ''}`}
            >
              {category}
            </button>
          ))}
        </div>
        <div className="card-grid">
          {featuredArticles.map((article) => (
            <article key={article.id} className="card">
              <span className="badge">{article.valuePropTag}</span>
              <h3>{article.title}</h3>
              <p>{article.excerpt}</p>
              <div className="trust-panel">
                <div>
                  <p className="trust-label">Source</p>
                  <strong>{article.source.outlet}</strong>
                  <p className="trust-hint">Model: {article.source.model}</p>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <p className="trust-label">Status</p>
                  <span className={`status-dot ${article.source.status}`}>{article.source.status}</span>
                  <a href={article.source.url} target="_blank" rel="noreferrer" className="cta-link">
                    View original
                  </a>
                </div>
              </div>
              <p className="trust-hint">{article.source.rewriteReason}</p>
              <footer className="card-footer">
                <small>Published {new Date(article.publishedAt).toLocaleDateString()}</small>
                <button type="button" className="ghost-button">
                  {article.cta.label}
                </button>
              </footer>
              <p className="trust-hint">{article.cta.explanation}</p>
            </article>
          ))}
        </div>
      </div>

      <div className="timeline">
        <h3>Featured production slots</h3>
        {featuredArticles.map((article, index) => (
          <div key={article.id} className="timeline-item">
            <time>{new Date(article.publishedAt).toLocaleDateString()}</time>
            <div>
              <p style={{ margin: 0, fontWeight: 600 }}>{article.category}</p>
              <p style={{ margin: '0.25rem 0 0', color: 'rgba(255,255,255,0.7)' }}>
                Slot #{index + 1}: {article.valuePropTag} via {article.source.model}
              </p>
            </div>
          </div>
        ))}
      </div>

      <div className="panel">
        <h2>Translation guardrail stack</h2>
        <p className="meta-note">
          Phase 010 tone & format guide enforces shared metadata, runtime limits, and reference docs for every copy block.
        </p>
        <div className="guardrail-grid">
          <article className="guardrail-card">
            <h4>필수 메타데이터</h4>
            <ul>
              {translationGuardrailStack.metadataFields.map((field) => (
                <li key={field}>{field}</li>
              ))}
            </ul>
            <p className="trust-hint">CTA footer: “Rewritten for Korean punchlines per translation guardrails.”</p>
          </article>
          <article className="guardrail-card">
            <h4>Runtime limits</h4>
            <p>
              Guardrail: {translationGuardrailStack.runtimeLimits.slaMinutes} min SLA ·{' '}
              {translationGuardrailStack.runtimeLimits.gpuHoursPerWeek} GPUh/wk
            </p>
            <p className="trust-hint">{translationGuardrailStack.modelPolicy}</p>
          </article>
          <article className="guardrail-card">
            <h4>Rewrite policy</h4>
            <p>{translationGuardrailStack.rewritePolicy}</p>
            <p className="trust-hint">
              Reference: {translationGuardrailStack.references.issues.join(', ')} ·{' '}
              <a className="cta-link" href={translationGuardrailStack.references.doc}>
                translation guardrails
              </a>
            </p>
          </article>
        </div>
      </div>

      <div className="panel">
        <h2>User journey messaging</h2>
        <p>Segments mapped to tone pillars with copy, proof hooks, and guardrail memos.</p>
        <div className="segment-grid">
          {journeyMessagingExamples.map((journey) => (
            <article key={journey.id} className="segment-card">
              <header>
                <h3>{journey.title}</h3>
                <p className="trust-hint">{journey.persona}</p>
              </header>
              <p className="segment-list">상황: {journey.situation}</p>
              <p className="segment-list">Copy: {journey.copy}</p>
              <p className="segment-list">Proof hook: {journey.proofHook}</p>
              <p className="segment-list">UI 위치: {journey.uiPlacement}</p>
              <p className="segment-list">Guardrail 메모: {journey.guardrailMemo}</p>
            </article>
          ))}
        </div>
      </div>

      {readinessLoaded && (
        <>
          <div className="panel">
            <h2>Phase 003~007 coverage</h2>
            <p>Every requirement from market synthesis through category architecture ships as structured API payloads.</p>
            <div className="phase-grid">
              {progress.map((phase) => (
                <article key={phase.identifier} className="phase-card">
                  <span className="phase-label">Phase {phase.phase}</span>
                  <h3>{phase.title}</h3>
                  <p>{phase.summary}</p>
                  <p className="phase-meta">Requirements: {phase.requirements.join(', ')}</p>
                  <p className="phase-meta">Capabilities: {phase.delivered_capabilities.join(', ')}</p>
                </article>
              ))}
            </div>
            <p className="meta-note">Synced via {readinessSource === 'api' ? 'live API' : 'embedded brief'} — {progress.length} phases ready.</p>
          </div>

          <div className="panel">
            <h2>Segment toggles & onboarding defaults</h2>
            <div className="segment-grid">
              {readiness.segments.map((segment) => (
                <article key={segment.segment} className="segment-card">
                  <header>
                    <h3>{segment.segment}</h3>
                    <p className="trust-hint">{segment.persona}</p>
                  </header>
                  <p className="segment-list">Pains: {segment.pains.join(', ')}</p>
                  <p className="segment-list">Gains: {segment.gains.join(', ')}</p>
                  <p className="segment-list">Toggles: {segment.toggles.join(', ')}</p>
                  <p className="segment-list">Needs: {segment.content_needs}</p>
                  <p className="segment-list">Tone: {segment.translation_tone}</p>
                  <p className="segment-list">
                    Monetization: {segment.monetization_hooks.join(', ')}
                  </p>
                  <p className="segment-list">
                    Notifications: {segment.onboarding_defaults.notifications.join(', ')}
                  </p>
                </article>
              ))}
            </div>
          </div>

          <div className="panel">
            <h2>Category architecture</h2>
            <div className="category-grid">
              {readiness.categories.metadata.map((category) => (
                <article key={category.id} className="category-card">
                  <header>
                    <h3>{category.title}</h3>
                    <p className="trust-hint">{category.tone}</p>
                  </header>
                  <p>Cadence: {category.cadence}</p>
                  <p>KPI tags: {category.kpi_tags.join(', ')}</p>
                  <p>Push default: {category.default_push}</p>
                  <p>CTA default: {category.default_cta}</p>
                  <p>
                    Performance:{' '}
                    {readiness.categories.performance[category.id]?.leading} ·{' '}
                    {readiness.categories.performance[category.id]?.lagging}
                  </p>
                </article>
              ))}
            </div>
            <div className="calendar-row">
              {readiness.categories.calendar.map((slot) => (
                <div key={slot.day} className="calendar-slot">
                  <strong>{slot.day}</strong>
                  <p>{slot.focus.join(', ')}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="panel">
            <h2>KPI & value prop snapshot</h2>
            <div className="kpi-grid">
              <div>
                <h3>KPI catalog</h3>
                <ul>
                  {readiness.kpi_catalog.items.map((item) => (
                    <li key={item.metric}>
                      <strong>{item.metric}</strong> — {item.type} ({item.target}) via {item.source}
                    </li>
                  ))}
                </ul>
              </div>
              <div>
                <h3>Value prop experiments</h3>
                <p className="trust-hint">Test window: {readiness.value_props.test_window_days} days</p>
                <ul>
                  {readiness.value_props.messages.map((message) => (
                    <li key={message.id}>
                      “{message.copy}” → {message.segments.join(', ')}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          {revenueLoaded && (
            <div className="panel">
              <h2>Phase 008 revenue hypotheses</h2>
              <p className="meta-note">
                Synced via {revenueSource === 'api' ? 'live API' : 'embedded blueprint'} · Approvals:{' '}
                {revenuePlan.approvals.decision_log.join(', ')}
              </p>

              <div className="hypothesis-grid">
                {revenuePlan.hypotheses.map((hypothesis) => {
                  const bundle = bundleLookup[hypothesis.bundle_id];
                  return (
                    <article key={hypothesis.hypothesis_id} className="hypothesis-card">
                      <header>
                        <span className="badge">{hypothesis.hypothesis_id}</span>
                        <h3>{hypothesis.title}</h3>
                      </header>
                      <p>{hypothesis.statement}</p>
                      <p className="trust-hint">Segments: {hypothesis.target_segments.join(', ')}</p>
                      <p className="trust-hint">Success: {hypothesis.success_metrics.join(' · ')}</p>
                      <p className="trust-hint">Evidence: {hypothesis.evidence.join(' / ')}</p>
                      {bundle && (
                        <p className="trust-hint">Bundle: {bundle.name}</p>
                      )}
                    </article>
                  );
                })}
              </div>

              <h3>Bundles & guardrails</h3>
              <div className="bundle-grid">
                {revenuePlan.bundles.map((bundle) => (
                  <article key={bundle.bundle_id} className="bundle-card">
                    <header>
                      <h4>{bundle.name}</h4>
                      <p className="trust-hint">Categories: {bundle.categories.join(', ')}</p>
                    </header>
                    <ul>
                      {bundle.deliverables.map((item) => (
                        <li key={item}>{item}</li>
                      ))}
                    </ul>
                    <p className="trust-hint">KPI: {bundle.kpi_reporting.join(', ')}</p>
                    <p className="trust-hint">Pricing: {bundle.pricing_model}</p>
                    <p className="trust-hint">Dependencies: {bundle.dependencies.join(', ')}</p>
                  </article>
                ))}
              </div>

              <h3>Experiment roadmap</h3>
              <div className="experiment-table-wrapper">
                <table className="experiment-table">
                  <thead>
                    <tr>
                      <th>Experiment</th>
                      <th>Metric</th>
                      <th>Schedule</th>
                      <th>Issues</th>
                    </tr>
                  </thead>
                  <tbody>
                    {revenuePlan.experiments.map((experiment) => (
                      <tr key={experiment.experiment_id}>
                        <td>
                          <strong>{experiment.experiment_id}</strong>
                          <p className="trust-hint">{experiment.hypothesis_id}</p>
                        </td>
                        <td>{experiment.goal_metric}</td>
                        <td>{experiment.schedule}</td>
                        <td>{experiment.issue_tags.join(', ')}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              <div className="guardrail-grid">
                <article className="guardrail-card">
                  <h4>Guardrails</h4>
                  <p>Model policy: {revenuePlan.guardrails.model_policy}</p>
                  <p>Source policy: {revenuePlan.guardrails.source_policy}</p>
                  <p>Cost ceiling: {revenuePlan.guardrails.cost_ceiling}</p>
                  <a className="cta-link" href={revenuePlan.guardrails.reference_doc}>
                    View translation guardrails
                  </a>
                </article>
                <article className="guardrail-card">
                  <h4>Dependencies</h4>
                  <ul>
                    {revenuePlan.dependencies.map((dependency) => (
                      <li key={dependency.id}>
                        <strong>{dependency.id}</strong>: {dependency.description} ({dependency.issue_tags.join(', ')})
                      </li>
                    ))}
                  </ul>
                </article>
              </div>
            </div>
          )}
        </>
      )}
    </section>
  );
};

export default Home;
